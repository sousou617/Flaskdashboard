#!/usr/bin/python3

from flask import Flask, render_template, url_for

app = Flask(__name__)
app.config['SERVER_NAME'] = 'localhost:5000'
#with open('myfile.json') as fi:
#	data = fi.readlines()

@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/login')
def about():
   return render_template('login.html')


#     @app.route('/data/<string:id>/')
# def SlaData(id):
#     return render_template('SLAdata.html', id=id)

with app.app_context():
	url_for('static', filename='css/style.css')

if __name__ == '__main__':
    app.run(debug=True)