from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/girl-power')
def hello_world():
    return render_template('Girl-power/index.html')
