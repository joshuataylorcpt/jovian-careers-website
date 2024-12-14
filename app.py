from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import create_engine, text
#need to create an app, object of the type class

app = Flask(__name__)

@app.route('/') #this is the empty route
def home():
    return render_template('home.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Get form data
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        # Insert data into the salesrequest table in MySQL
        with engine.connect() as conn:
            insert_query = """
            INSERT INTO salesrequest (first_name, last_name, email, phone, message, created_at)
            VALUES (:first_name, :last_name, :email, :phone, :message, :created_at)
            """
            # Prepare the data to insert
            conn.execute(text(insert_query), {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone': phone,
                'message': message,
                'created_at': datetime.now()
            })

        # Optionally, you can redirect or show a success message
        return render_template('contact.html', success=True)

    # For GET requests, just render the contact form
    return render_template('contact.html')
    
    
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)