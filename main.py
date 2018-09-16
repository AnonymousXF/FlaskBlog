# -*- coding: UTF-8 -*-
from flask import Flask, render_template
from config import *

app = Flask(__name__)
#app.config.from_object(DevConfig)

@app.route('/')
def index():
    file = open("D:\README.md", 'r', encoding="utf-8")
    md = file.read()
    file.close()
    return render_template('index.html', markdown=md)

if __name__ == "__main__":
    app.run()
