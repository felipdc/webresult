from flask import Flask, render_template, send_from_directory
import pandas as pd
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/displaydata')
def displaydata():
    table = pd.read_csv("time_rc5.csv")
    return render_template('displaydata.html', data=table.to_html())

@app.route('/getdata/<string:file>')
def testdata(file):
    return send_from_directory('', file)
