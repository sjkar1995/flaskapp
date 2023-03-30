from flask import Flask,render_template,request
import pyodbc
ccnn=pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-GJ0PM7F\SQLEXPRESS;DATABASE=test;')
#change
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
@app.route('/home')
def index():
    return render_template('home.html',username="satya")
@app.route('/submit-form',methods=['POST', 'GET'])
def formdata():
    uname = request.form['name']
    email = request.form['email']
    return render_template('form.html',gname=uname,gemail=email)
