import json
import pandas as pd
from flask import Flask, make_response, jsonify, request, render_template
import cx_Oracle
import sqlalchemy as sa


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("chartist.html")

if __name__ == '__main__':
    app.debug = True
    app.run()
