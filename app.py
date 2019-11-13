import os
import json
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models import temperatures, engine

import dateutil.parser

app = Flask(__name__)
with open("config.json") as fp :
    config = json.load(fp)

app.config.from_object(config['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/api/v0.1/temperature", methods=['GET', 'PUT'])
def temperature():
    if request.method == 'PUT':
        tmps = request.json
        sensor_id = tmps["sensor_id"]
        tmp = tmps["temperature"]
        timestamp = dateutil.parser.parse(tmps["timestamp"])
        conn = engine.connect()
        conn.execute(temperatures.insert().values(sensor_id=sensor_id, temperature=tmp, timestamp=timestamp))
        return 'ok'
    elif request.method == 'GET':
        conn = engine.connect()
        r = conn.execute(temperatures.select())
        return {'temperatures': list(r)}

    else:
        return "Cette partie est en cours de réalisation !!!!"


if __name__ == '__main__':
    app.run()
