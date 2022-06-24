import json
import pandas as pd
from flask import Flask, make_response, jsonify, request, render_template
import cx_Oracle
import sqlalchemy as sa
import numpy as np


def getList(s_production):

    engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
    conn = engine.connect()

    df1 = pd.read_sql(f"seljuect * from bank_all where 상품명 like '%{s_production}%' " , conn)


    json_str1 = df1.to_json(orient="values")
    json_obj1 = json.loads(json_str1)


    return json_obj1


if __name__ == '__main__':
    arr = getList('디딤')
    arr = np.array(arr)
    print(arr)
