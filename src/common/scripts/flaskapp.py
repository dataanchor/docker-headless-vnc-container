import os
import sys
from flask import Flask, make_response, jsonify
app = Flask(__name__)

libreOfficeTypes = set(['doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx'])
imageTypes = set(['png', 'jpg', 'jpeg'])    

@app.route("/")
def hello():
    return "hello"

@app.route("/file/<fileName>")
def open_file(fileName):
    
    if '.' in fileName:
        fileType = fileName.rsplit('.', 1)[1].lower()
    
    try:
        if fileType in libreOfficeTypes:
            # sudo apt-get install libreoffice
            command = "libreoffice /logs/$POD_NAME/" + fileName + ' &'
            response = os.system(command)
            return response, 200
        elif fileType == 'pdf':
            # sudo apt-get install mupdf mupdf-tools
            command = "mupdf /logs/$POD_NAME/" + fileName +' &'
            response = os.system(command)
            return response, 200
        elif fileType == 'txt':
            # sudo apt install gedit gedit-plugins gedit-common
            command = "gedit /logs/$POD_NAME/" + fileName +' &'
            response = os.system(command)
            return response, 200
        elif fileType in imageTypes:
            # sudo apt-get install eog
            command = "eog /logs/$POD_NAME/" + fileName +' &'
            response = os.system(command)
            return response, 200
        else:
            response = make_response(jsonify(message="File type not supported"))
            return response, 500
    except:
        e = sys.exc_info()[0]
        return e, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0')