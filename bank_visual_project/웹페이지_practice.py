import json
import pandas as pd
from flask import Flask, make_response, jsonify, request, render_template
import cx_Oracle
import sqlalchemy as sa

engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
conn = engine.connect()
#
# bank = pd.read_csv('./우리은행_보도자료.csv')
# bank.to_sql("woori", conn)

#bank2 = pd.read_csv('./하나은행_보도자료.csv')
# bank2.to_sql("hana", conn)

app = Flask(__name__)

@app.route('/')
def index():

    engine = sa.create_engine('oracle://ai:0000@localhost:1521/XE')
    conn = engine.connect()
    df2 = pd.read_sql("select * from hana WHERE ROWNUM < 10", conn)
    df3 = pd.read_sql("select * from woori WHERE ROWNUM < 10", conn)

    json_str = df2.to_json(orient="values")
    json_obj = json.loads(json_str)

    json_str2 = df3.to_json(orient="values")
    json_obj2 = json.loads(json_str2)


    return render_template("index.html",
                           MY_NEWS_HANA = json_obj,
                           MY_NEWS_WOORI = json_obj2)



@app.route('/gopage')
def gopage():
    return render_template("국민은행.html")

@app.route('/ggopage')
def ggopage():
    return render_template("신한은행.html")

@app.route('/gggopage')
def gggopage():
    return render_template("우리은행.html")

@app.route('/ggggopage')
def ggggopage():
    return render_template("하나은행.html")

@app.route('/backpage')
def backpage():
    return render_template("index.html")

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






