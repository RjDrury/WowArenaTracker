import requests
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:postgres@localhost:5433/wow_arena_tracker_dev'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

bcrypt = Bcrypt(app)

from route import *

if __name__ == '__main__':
    app.secret_key = "top_secret"
   # db.create_all()
    app.run()


