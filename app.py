from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
#need to create an app, object of the type class

app = Flask(__name__)

@app.route('/') #this is the empty route
def home():
    return render_template('home.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
    
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)