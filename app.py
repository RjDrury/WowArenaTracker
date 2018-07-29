import requests
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:postgres@localhost:5433/wow_arena_tracker_dev'
manager = Manager(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db',MigrateCommand)
port = int(os.environ.get('PORT', 5000))


bcrypt = Bcrypt(app)

from route import *

if __name__ == '__main__':
    app.secret_key = "top_secret"
   # db.create_all()
    manager.run()
    app.run(host='0.0.0.0', port=port)

#import os from pml import app port = int(os.environ.get('PORT', 5000)) app.run(host='0.0.0.0', port=port)


