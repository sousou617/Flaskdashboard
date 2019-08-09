#!/usr/bin/python3
from flask_bootstrap import Bootstrap
import matplotlib.pyplot as plt
import numpy as np 
import random
from flask import Flask, render_template, url_for


app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:5000'

Bootstrap(app)


@app.route('/')
def home():
    return render_template('home.html', argument_dict)

@app.route('/login')
def about():
   return render_template('login.html')



with app.app_context():
	url_for('static', filename='css/style.css')

if __name__ == '__main__':
    app.run(debug=True)