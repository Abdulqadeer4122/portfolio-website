from flask import Flask,render_template, redirect, request ,url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField,TimeField,SelectField,TextAreaField
from wtforms.validators import DataRequired
import requests
import smtplib
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
bootstrap=Bootstrap5(app)

SENDER_PASSWRD='qiqe nxmf modd twfa'
SENDER_EMAIL="abdul.qadeer4122@gmail.com"


class ContactForm(FlaskForm):
    name=StringField("Enter Your Name",validators=[DataRequired()])
    email=StringField("Enter Your Email",validators=[DataRequired()])
    mesage=TextAreaField("Enter Your Message", validators=[DataRequired()])
    submit=SubmitField("Enter")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact' ,methods=['GET','POST'])
def contact():
    if request.method=='POST':
        with smtplib.SMTP('smtp.gmail.com', 587) as con:
            con.starttls()
            con.login(SENDER_EMAIL, SENDER_PASSWRD)
            con.sendmail(SENDER_EMAIL, SENDER_EMAIL, msg=request.form.get('message'))
            con.close()
            return redirect(url_for("home"))
    return render_template('contact.html')
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')
if __name__=="__main__":
    app.run(debug=True)