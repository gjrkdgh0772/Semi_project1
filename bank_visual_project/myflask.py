import json
import pandas as pd
from flask import Flask, make_response, jsonify, request, render_template
import cx_Oracle
import sqlalchemy as sa
import numpy as np
from 시각화.mytest import getList

app = Flask(__name__)


@app.route('/')
def myindex():

    return render_template('index2.html')


@app.route('/list', methods=['get', 'post'])
def mylist():

    engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
    conn = engine.connect()

    s_production = request.form["s_production"]
    list = getList(s_production)


    return render_template('stock.html', S_list = list, s_production=s_production
                                        )


if __name__ == '__main__':
    app.run(host="127.0.0.1", port='80')