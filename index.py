from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def eat():
    return render_template('index.html')

@app.route('/list')
def list():
    print("list....")
