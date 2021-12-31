from flask import Flask, request, render_template, redirect, url_for,session
import pickle
from model import model
import numpy as np
from wtforms import StringField, PasswordField, BooleanField, SubmitField,IntegerField,FloatField,SelectField
from wtforms.validators import DataRequired, InputRequired, Length, NumberRange
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap=Bootstrap(app)