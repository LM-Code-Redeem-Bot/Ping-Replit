from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def hello():
    l=list(os.getenv('urls').split(','))
    import requests
    for i in l:
      try:
        res=requests.get(i, timeout=1)
        print(i,res.text) 
      except:
        print("Ping Successful")
    return 'Ping Successful'

