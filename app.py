from flask import Flask, render_template

#need to create an app, object of the type class

app = Flask(__name__)

@app.route('/') #this is the empty route
def hello_jovian():
    return render_template('home.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)