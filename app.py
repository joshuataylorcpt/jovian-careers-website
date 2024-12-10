from flask import Flask

#need to create an app, object of the type class

app = Flask(__name__)

@app.route('/') #this is the empty route
def hello_world():
    return 'Hello, world!'

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)