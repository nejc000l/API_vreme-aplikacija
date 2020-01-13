from random import randint

from flask import Flask, render_template
import requests
import os
app=Flask(__name__)

try:
    API_KEY = os.environ ["API_KEY"]
except:
    API_KEY = open("API_KEY.txt").read().strip()



URL= f"https://api.openweathermap.org/data/2.5/weather?q=London&appid={API_KEY}&units=metric"




@app.route("/", methods=["GET"])
def index():
    ime_mesta=["Ljubljana", "London", "Paris"][randint(0,2)]
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={ime_mesta}&appid={API_KEY}&units=metric"

    result= requests.get(URL).json()

    return render_template("index.html", data= result)









if __name__ == '__main__':
    app.run()