# -*- coding: utf-8 -*-
from wtforms import StringField, PasswordField, BooleanField, SubmitField,IntegerField,FloatField,SelectField
from wtforms.validators import DataRequired, InputRequired, Length, NumberRange
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
       GRE = IntegerField('GRE', validators=[InputRequired(),NumberRange(min=280,max=340,message="Input is not a valid score")],render_kw={'placeholder': '300'})
       TOEFL = IntegerField('TOEFL', validators=[InputRequired(),NumberRange(min=0,max=120,message="Input is not a valid score")],render_kw={'placeholder': '100'})
       university_rank = SelectField('University Ranking From US News',choices=[('5','1-20'),('4','20-40'),('3','40-60'),('2','60-80'),('1','>80')])
       personal_statement_strength =  SelectField('PS Strength',choices=[(5,'Very Strong'),(4,'Strong'),(3,'Medium'),(2,'Not So Competitive'),(1,'Boring Paper Work')])
       recommendation_strength =  SelectField('Recommendation Letter Strength',choices=[(5,'Very Strong'),(4,'Strong'),(3,'Medium'),(2,'Not So Competitive'),(1,'Boring Paper Work')])
       GPA = FloatField(label="CGPA",validators=[InputRequired(),NumberRange(min=0,max=10.0,message="Input is not a valid score")],render_kw={'placeholder': '7'})
       research_original=SelectField('Recommendation Letter Strength',choices=[(1,'Yes'),(0,'No')])
       submit = SubmitField('Prediction')