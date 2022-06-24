import json
import pandas as pd
from flask import Flask, make_response, jsonify, request, render_template
import cx_Oracle
import sqlalchemy as sa

#
# engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
# conn = engine.connect()
# kb1 = pd.read_csv('./국민_예금.csv')
# kb1.to_sql("kb1", conn)
#
# engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
# conn = engine.connect()
# kb2 = pd.read_csv('./국민_적금.csv')
# kb2.to_sql("kb2", conn)
#
# engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
# conn = engine.connect()
# kb3 = pd.read_csv('./국민_대출.csv')
# kb3.to_sql("kb3", conn)

# engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
# conn = engine.connect()
# woori2 = pd.read_csv('./우리_적금.csv')
# woori2.to_sql("woori2", conn)
#
# engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
# conn = engine.connect()
# woori3 = pd.read_csv('./우리_대출.csv')
# woori3.to_sql("woori3", conn)


# engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
# conn = engine.connect()
# shinhan2 = pd.read_csv('./신한_적금.csv')
# shinhan2.to_sql("shinhan2", conn)

# engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
# conn = engine.connect()
# shinhan3 = pd.read_csv('./신한_대출.csv')
# shinhan3.to_sql("shinhan3", conn)

# engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
# conn = engine.connect()
# bank = pd.read_csv('./서민대출.csv')
# bank.to_sql("서민대출", conn)


# engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
# conn = engine.connect()
# bank = pd.read_csv('./우리_정형데이터.csv')
# bank.to_sql("woori", conn)

# engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
# conn = engine.connect()
# bank = pd.read_csv('./제품/국민_신용대출.csv')
# bank.to_sql("국민_신용대출", conn)

# engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
# conn = engine.connect()
# bank = pd.read_csv('./제품/국민_예적금.csv')
# bank.to_sql("국민_예적금", conn)
#
# engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
# conn = engine.connect()
# bank = pd.read_csv('./제품/신한_신용대출.csv')
# bank.to_sql("신한_신용대출", conn)
#
# engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
# conn = engine.connect()
# bank = pd.read_csv('./제품/신한_예적금.csv')
# bank.to_sql("신한_예적금", conn)
#
# engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
# conn = engine.connect()
# bank = pd.read_csv('./제품/우리_신용대출.csv')
# bank.to_sql("우리_신용대출", conn)
#
# engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
# conn = engine.connect()
# bank = pd.read_csv('./제품/우리_예적금.csv')
# bank.to_sql("우리_예적금", conn)
#
# engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
# conn = engine.connect()
# bank = pd.read_csv('./제품/하나_신용대출.csv')
# bank.to_sql("하나_신용대출", conn)
#
# engine = sa.create_engine('oracle://test:0000@localhost:1521/XE')
# conn = engine.connect()
# bank = pd.read_csv('./제품/하나_예적금.csv')
# bank.to_sql("하나_예적금", conn)

