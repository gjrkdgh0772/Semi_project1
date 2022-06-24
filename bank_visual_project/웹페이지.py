import json
import pandas as pd
from flask import Flask, make_response, jsonify, request, render_template
# import cx_Oracle
# import sqlalchemy as sa


# engine = sa.create_engine('oracle://ai:0000@localhost:1521/XE')
# conn = engine.connect()
# bank1 = pd.read_csv('./하나_예금.csv')
# bank1.to_sql("hana1", conn)
# bank2 = pd.read_csv('./하나_적금.csv')
# bank2.to_sql("hana2", conn)
# bank3 = pd.read_csv('./하나_대출.csv')
# bank3.to_sql("hana3", conn)

app = Flask(__name__)




@app.route('/')
def index():

    engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
    conn = engine.connect()


    df1 = pd.read_sql('select * from bank1' , conn)
    df2 = pd.read_sql('select * from bank2 order by 이자율 asc' , conn)
    df3 = pd.read_sql('select * from bank3 order by 한도 desc' , conn)

    json_str1 = df1.to_json(orient="values")
    json_obj1 = json.loads(json_str1)

    json_str2 = df2.to_json(orient="values")
    json_obj2 = json.loads(json_str2)

    json_str3 = df3.to_json(orient="values")
    json_obj3 = json.loads(json_str3)


    return render_template("index.html" ,
                           MY_BANK1 = json_obj1,
                           MY_BANK2 = json_obj2,
                           MY_BANK3 = json_obj3
                           )

@app.route('/gopage')
def gopage():

    engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
    conn = engine.connect()

    df111 = pd.read_sql('select * from kb1' , conn)
    df222 = pd.read_sql('select * from kb2 where rownum <= 7 order by 이자율 asc' , conn)
    df333 = pd.read_sql('select * from kb3 where rownum <= 7 ' , conn)

    json_str111 = df111.to_json(orient="values")
    json_obj111 = json.loads(json_str111)

    json_str222 = df222.to_json(orient="values")
    json_obj222 = json.loads(json_str222)

    json_str333 = df333.to_json(orient="values")
    json_obj333 = json.loads(json_str333)

    return render_template("국민은행.html" ,  MY_KB1 = json_obj111,
                           MY_KB2 = json_obj222, MY_KB3 = json_obj333)



    # engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
    # conn = engine.connect()
    # df2 = pd.read_sql("select 총자산 from kb", conn)

    #
    #
    # print(f"df2.columns: {df2.columns.values}")
    # print(f"df2.values.tolist(): {df2.values.tolist()}")
    #
    # title = df2.columns.values
    # d_data = df2.values.tolist()
    # my_list = []
    # my_list.append(title)
    # my_list.append(d_data)



    # MY_LABEL = column_name
    # return render_template("국민은행.html")
                           # , MY_DATA=my_list)
                           # MY_NEWS_WOORI = json_obj2)

@app.route('/ggopage')
def ggopage():

    engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
    conn = engine.connect()

    df4 = pd.read_sql('select * from shinhan1' , conn)
    df5 = pd.read_sql('select * from shinhan2 where rownum <= 7 order by 이자율 asc' , conn)
    df6 = pd.read_sql('select * from shinhan3 where rownum <= 7 ' , conn)

    json_str4 = df4.to_json(orient="values")
    json_obj4 = json.loads(json_str4)

    json_str5 = df5.to_json(orient="values")
    json_obj5 = json.loads(json_str5)

    json_str6 = df6.to_json(orient="values")
    json_obj6 = json.loads(json_str6)

    return render_template("신한은행.html" ,  MY_SHINHAN1 = json_obj4,
                           MY_SHINHAN2 = json_obj5, MY_SHINHAN3 = json_obj6)

@app.route('/gggopage')
def gggopage():

    engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
    conn = engine.connect()

    df4 = pd.read_sql('select * from woori1' , conn)
    df5 = pd.read_sql('select * from woori2 where rownum <= 7 order by 이자율 asc' , conn)
    df6 = pd.read_sql('select * from woori3 where rownum <= 7 ' , conn)

    json_str4 = df4.to_json(orient="values")
    json_obj4 = json.loads(json_str4)

    json_str5 = df5.to_json(orient="values")
    json_obj5 = json.loads(json_str5)

    json_str6 = df6.to_json(orient="values")
    json_obj6 = json.loads(json_str6)

    return render_template("우리은행.html" ,  MY_WOORI1 = json_obj4,
                           MY_WOORI2 = json_obj5, MY_WOORI3 = json_obj6)




@app.route('/ggggopage')
def ggggopage():

    engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
    conn = engine.connect()

    df20 = pd.read_sql('select * from hana1' , conn)
    df21 = pd.read_sql('select * from hana2 where rownum <= 7 ' , conn)
    df22 = pd.read_sql('select * from hana3 where rownum <= 7 ' , conn)

    json_str20 = df20.to_json(orient="values")
    json_obj20 = json.loads(json_str20)

    json_str21 = df21.to_json(orient="values")
    json_obj21 = json.loads(json_str21)

    json_str22 = df22.to_json(orient="values")
    json_obj22 = json.loads(json_str22)

    return render_template("하나은행.html" ,  MY_HANA1 = json_obj20,
                           MY_HANA2 = json_obj21, MY_HANA3 = json_obj22)



@app.route('/backpage')
def backpage():
    engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
    conn = engine.connect()


    df1 = pd.read_sql('select * from bank1' , conn)
    df2 = pd.read_sql('select * from bank2 order by 이자율 asc' , conn)
    df3 = pd.read_sql('select * from bank3 order by 한도 desc' , conn)

    json_str1 = df1.to_json(orient="values")
    json_obj1 = json.loads(json_str1)

    json_str2 = df2.to_json(orient="values")
    json_obj2 = json.loads(json_str2)

    json_str3 = df3.to_json(orient="values")
    json_obj3 = json.loads(json_str3)

    return render_template("index.html" ,
                           MY_BANK1 = json_obj1,
                           MY_BANK2 = json_obj2,
                           MY_BANK3 = json_obj3
                           )




if __name__ == '__main__':
    app.debug = True
    app.run()





# #=============================================== form post
# @app.route('/form_submit_post', methods=["post"])
# def form_submit_post():
#     # 웹페이지 <form>에서 넘어온 값
#     # http://192.168.0.44:9999/form_submit_post
#     userid = request.form.get("userid")  #name="userid"
#     userpw = request.form.get("userpw")
#
#     print("form_submit_post.........실행", userid, userpw)
#     return render_template("ajax_test_result.html",MY_MSG="ok")
#
# #=============================================== form get
# @app.route('/form_submit_get', methods=["get"])
# def form_submit_get():
#     # 웹페이지 <form>에서 넘어온 값
#     # http://192.168.0.44:9999/form_submit_get?userid=kim&userpw=111
#     userid = request.args.get("userid")  # name="userid"
#     userpw = request.args.get("userpw")
#
#     print("form_submit_get.........실행", userid, userpw)
#     return render_template("ajax_test_result.html", MY_MSG="ok")
#
#
# @app.route('/form_ajax', methods=["post"])
# def form_ajax():
#     # 웹페이지 <form>에서 넘어온 값 json
#     data = request.get_data()
#     print("form_ajax.........실행", data)
#
#     # list = [["smith", 1400],
#     #         ["allen", 4000],
#     #         ]
#     list = [{"ename": "smith", "sal": 1400},
#             {"ename": "allen", "sal": 4000}
#             ]
#     list_str = json.dumps(list)
#     print("list_str", list_str)
#     return list_str






