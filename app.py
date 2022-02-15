from scrap import scrapper
from flask import Flask,render_template
import time

app=Flask(__name__)
a=scrapper()



@app.route('/')
def hello():
    return (render_template('index.html'))

@app.route('/get_dji')
def send_dji():
    result_flag = a.get_dji()
    return (a.dji)


@app.route('/get_hsi')
def send_hsi():
    result_flag = a.get_hsi()
    return (a.hsi)


@app.route('/get_gold')
def send_gold():
    result_flag = a.get_gold()
    return (a.gold)