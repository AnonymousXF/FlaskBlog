#_*_coding:utf-8_*_
from flask import Flask, render_template
from config import *

app = Flask(__name__)
app.config.from_object(DevConfig)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
