from flask_ext import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import json

from app import app, db

with open("config.json") as fp :
    config = json.load(fp)

app.config.from_object(config['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
