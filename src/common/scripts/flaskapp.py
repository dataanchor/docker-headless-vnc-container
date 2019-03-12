import os
import sys
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"

@app.route("/file/<fileName>")
def open_file(fileName):
    try:
        command = "google-chrome /logs/$POD_NAME/" + fileName +' &'
        response = os.system(command)
        return response
    except:
        e = sys.exc_info()[0]
        return e

if __name__ == '__main__':
    app.run(host='0.0.0.0')