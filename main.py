
from random import randint
from flask import Flask
app = Flask('app')

@app.route('/')
def hello_world():
  banana = randint(0,5)
  return '<h1>Hello, World!</h1>'+str(banana)

@app.route('/banana')
def banana():
  banana = randint(0,5)
  return 'banana'+str(banana)

app.run(host='0.0.0.0', port=8080)