from flask import Flask
from flask import json
import time
import logging

logging.basicConfig(filename='app.log',level=logging.DEBUG)

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info('Main request successfull')
    return "Hello World!"

@app.route("/status")
def status():

    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    
    app.logger.info('Status request successfull')
    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({"data": {"UserCount": 140, "UserCountActive": 23}}),
        status=200,
        mimetype='application/json'
    )

    app.logger.info('Metrics request successfull')
    return {"data": {"UserCount": 140, "UserCountActive": 23}}

if __name__ == "__main__":
    app.run(host='0.0.0.0')
