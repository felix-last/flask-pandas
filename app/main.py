from flask import Flask, send_file
import pandas as pd

app = Flask(__name__)
@app.route('/')
def index():
    return 'Hi! Flask-pandas is running! Mount app/ containing main.py to /app'
