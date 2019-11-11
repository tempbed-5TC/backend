import os
import json
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




app = Flask(__name__)
with open("config.json") as fp :
    config = json.load(fp)

app.config.from_object(config['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route("/api/v0.1/temperature", methods=['GET','PUT'])
def temperature() :
    if request.method == 'PUT':
        tmps = request.json
        id = tmps["sensor_id"]
        tmp = tmps["temperature"]
        timestamp = tmps["timestamp"]
        db(id,tmp,timestamp)
    else:
        return "Cette partie est en cours de réalisation !!!!"

if __name__ == '__main__':
    app.run()
