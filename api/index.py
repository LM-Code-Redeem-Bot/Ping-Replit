from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def hello():
    l=list(os.getenv('urls').split(','))
    import requests
    for i in l:
      res=requests.get(i)
      print(i,res.text) 
    return 'Ping Successful'

