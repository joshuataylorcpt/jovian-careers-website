from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

# Create an app object of the Flask class
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Pricing route
@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

# Contact route (GET and POST requests)
@app.route('/contact')
def contact():
    # For GET requests, just render the contact form
    return render_template('contact.html')

@app.route('/ourservices')
def our_services():
    return render_template('ourservices.html')


# Ensure app runs on the specified host and port, with debug mode enabled

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
