import json
import math
from random import Random
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return jsonify({"Név": "Pál", "Életkor": Random().randint(18, 80)})


app.run()
