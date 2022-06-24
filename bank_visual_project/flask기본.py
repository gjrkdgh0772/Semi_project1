import json

import pandas as pd
from flask import Flask, make_response, jsonify, request, render_template
import cx_Oracle
import sqlalchemy as sa

# ------------------------------------
# pip install flask_cors
from flask_cors import CORS, cross_origin
# CORS(app)
# CORS(app, resources={r'*': {'origins': '*'}})
# ------------------------------------

# Flask : class 생성자(app)를 만들어서 사용.
app = Flask(__name__) #, template_folder="", static_folder="")
CORS(app)

def my_news_realmeter():
    # to_sql(table_name, sqlalchemy.conn만가능)
    engine = sa.create_engine('oracle://ai:0000@localhost:1521/XE')
    conn = engine.connect()

    url = "http://www.realmeter.net/category/politics/"
    res = requests.get(url)

    soup = BeautifulSoup(res.text, "html.parser", )
    box_list = soup.select("body > div > div.main.wrap.cf > div > div > div.posts-list.listing-alt > article")

    # ----------------------------------------------------list[list]
    tot_list = []
    for box in box_list:
        list = []
        rdate = box.select_one("div > time").text
        title = box.select_one("div > a").text
        href = box.select_one("div > a").get("href")
        content = box.select_one("div > div > p").text
        pic = box.select_one("a > img").get("src")
        list.append(rdate)
        list.append(title)
        list.append(href)
        list.append(content)
        list.append(pic)
        tot_list.append(list)

    df = pd.DataFrame(data=tot_list,
                      columns=["rdate", "title", "href", "content", "pic"]
                      # dtype={"a":'int64', "b":'int64', "c":'object' }
                      )
    # 자동으로 테이블을 만들어 준다. 단.. 기존에 만들어져 있으면 에러가 난다.
    df.to_sql("news_realmeter", conn)  # if_exists: str = "fail"
    print("=============done======", len(tot_list))
# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# @app.route('/')
# def hello():
#    return 'hello world'

@app.route('/')    # 괄호안에 '/abc'라고 붙어있으면 주소창에서도 똑같이 /abc를 입력해줘야 한다.
def index():
    mylist = [1, 2, 3]
    point = 10000

    engine = sa.create_engine('oracle://ai:0000@localhost:1521/XE')
    conn = engine.connect()
    df = pd.read_sql("select * from news_realmeter", conn)
    html = df.to_html()

    json_str = df.to_json(orient="values")  # <class str>
    json_obj = json.loads(json_str)         # <class list> [[10,20,30], [1,2,3]] == df.values.tolist()
    # str_json = json.dumps(json_obj)
    return render_template("index.html",
                           MY_NEWS=json_obj)  # Flask는 web에 보낼 때, 객체(obj)를 보내는 것이 가능.


# ------------- 업체이름을 타이핑할때마다 실시간 비동기로 업체 명단을 가져와서 리턴 ---------------------
@app.route('/com_search_ajax', methods=['gett'])
def com_search_ajax():         # 함수명도 겹치면 안되고, 주소창도 겹치면 안된다.


    # --------------------------------------------------------------------
    # 네이버 금융 : 시황 업체 목록 가져오기
    # 네이버 증권사 : ISO-8859-1
    url = "http://comp.fnguide.com/XML/Market/CompanyList.txt"
    com_res = requests.get(url)

    com_res.encoding = "utf-8-sig"
    com_json = json.loads(com_res.text)  # com_json = {"Co : [ {},{},{} ] }

    com_df = pd.read_csv("com_df.csv")

    # -------------------- 웹에서 입력한 검색어와 관련된 업체만 가져오기 ----------
    str = request.form.get("search_input")
    temp = com_df[["cd", "nm"]][com_df["nm"].str.contains(str)].head()
    print(temp.values.tolist())
    return json.dumps(temp.values.tolist())


# java : void main()
if __name__ == '__main__':
    app.debug = True    # ERROR 코드 리스트를 보여줌. 마무리 할 때는 막아주기.
    app.run(host='0.0.0.0', port=80)
    # 0.0.0.0 : ipconfig ipv4 / 127.0.0.1 : local host, port = (기본 : 80) or (무작위 4자리 숫자)
    # Flask(__lec20_flask.py__).run(web으로 구동시켜라)

    # http: // 192.168.0.11:80 / 에서 index.html 읽어오기