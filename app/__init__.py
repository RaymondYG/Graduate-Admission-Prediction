from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('setting.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

from app import views 

