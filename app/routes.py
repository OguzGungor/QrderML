from .ml import *
from .db import *
from app import app
from flask import request


@app.route('/')
@app.route('/asd')
def index():
    return "Hello, World!"

#test route
@app.route("/test",methods=["POST"])
def test():
    return "here : " + str(testFunc(request.json["id"]))
    #return request.json['name']
