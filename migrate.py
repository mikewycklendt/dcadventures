from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from dotenv import load_dotenv()
load_dotenv()
import os

db_path = os.environ.get("db_path")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_path

db = SQLAlchemy(app)

# Import database models with app context
with app.app_context():
  from models import *

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()

'''
sudo python3 migrate.py db migrate
sudo python3 migrate.py db upgrade
'''