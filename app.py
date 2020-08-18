from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import Form, FloatField, SubmitField, validators, ValidationError
from form import BMIform

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret key'
app.config['WTF_CSRF_ENABLED'] = True

@app.route('/')
def index():
    form = BMIform(request.form)
    return render_template('index.html',form=form)

@app.route('/',methods=['POST'])
def BMI():
    form = BMIform(request.form)
    if request.method == "POST":
        if form.validate() == False:
            message = "you false"
            return render_template('index.html',form=form)

        else:
            form = BMIform(request.form)
            result = ''
            weight = request.form.get('weight', type=float)
            height = request.form.get('height', type=float)
            result = weight / (height/100) ** 2
            return render_template('index.html',result=result, form=form, result_message="あなたのBMIは%0.2fです" % result) 

if __name__ == '__main__':
    app.run()
    # app.debug = True
    # app.run(host='localhost')
