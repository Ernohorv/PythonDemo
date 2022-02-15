import json
import math
from random import Random
from flask import Flask, request, jsonify, after_this_request

app = Flask(__name__)


def mod(value):
    return value


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city = request.form.get('city')
        return '''
                <h1>The City is {}</h1>'''.format(city)

    return '''
              <form method="POST">
              <center>
                  <div><label>City: <input type="text" name="city"></label></div>
                  <br></br>
                  <input type="submit" value="Submit" style="align:center">
                  </center>
              </form>'''


app.run()
