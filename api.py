import requests
from flask import Flask, render_template,request
import json
import time
import datetime
app = Flask(__name__)

r = requests.get("http://data.fixer.io/api/latest?access_key=9d2079c681004ae6b2e44bd93c43af7c")
r = r.json()
@app.route('/')
def hello_world():

    return render_template('index.html',Time=time)


@app.route('/convert',methods=['POST'])
def convert():
    #r = requests.get("http://data.fixer.io/api/latest?access_key=9d2079c681004ae6b2e44bd93c43af7c")
    #r = r.json()
    currency_data = r['rates']

    input_amount = int(request.form['amount'])
    input_currency_value = currency_data[request.form['currency'].upper()]
    input_currency = request.form['currency'].upper()
    #print(input_amount,input_currency)
    conversion = input_amount*input_currency_value
    time.sleep(1)


    return render_template('result.html',result=round(conversion,3),currency=input_currency,amount=input_amount)


@app.route('/currency_rates')
def currency_list():
    currency_data = r['rates']
    time.sleep(1)
    return render_template('all_amounts.html',names = currency_data)




if __name__ == "__main__":
    app.run(debug=True)