from flask_wtf import FlaskForm
from wtforms import Form, FloatField, SubmitField, validators, ValidationError

class BMIform(Form):
    weight = FloatField('weight', [validators.InputRequired("all parameters are required!")])
    height = FloatField('height',[validators.InputRequired("all parameters are required!")])
    submit = SubmitField('計算')
    
