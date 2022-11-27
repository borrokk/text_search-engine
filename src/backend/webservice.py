"""webservice.py """

from flask import Flask, jsonify, request 
import json 
import predictor

app= Flask(__name__)

@app.route('/')
def service_status(): 
  return 'Service is up!'

@app.errorhandler(404) 
def page_not_found(exception): 
  return exception

@app.route("/search', methods-['GET']) 
def process(): 
  query= request.args.get('query') 
  response = predictor.predict(query) 
  print(response) 
  json_str = response.to_dict() 
  str= json.dumps(json_str) 
  #dictionary = json.loads(str) 
  return str 

if name --'_main_': 
  app.run(host-'0.0.0.0')
