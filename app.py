import json
import math
from random import Random
from flask import Flask, request, jsonify, after_this_request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city = request.form.get('city')
        response = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID=6364d96eff37ce254aeabb6fcccd9740&units=metric")
        content = json.loads(response.text)

        if response.status_code == 200:
            temp = content["main"]["temp"]
            feels_like = content["main"]["feels_like"]
            char = content["weather"][0]["description"]

            return '''
                    <center>
                    <h1>The City is {}</h1>
                    <p>The temperature is {}°</p>
                    <p>The temperature feels like {}°</p>
                    <p>The characteristic of the weather: {}</p>
                    <button onClick="window.history.back()">Back</button>
                     </center>'''.format(city, temp, feels_like, char)
        else:
            return '''
             <center>
                    <h1>Wrong city name</h1>
                    <button onClick="window.history.back()">Back</button>
                    </center>
            '''

    return '''
              <form method="POST">
              <center>
                  <div><label>City: <input type="text" name="city"></label></div>
                  <br></br>
                  <input type="submit" value="Submit" style="align:center">
                  </center>
              </form>'''


app.run()
