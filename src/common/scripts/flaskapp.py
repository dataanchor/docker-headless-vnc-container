import os
import subprocess
import sys
from flask import Flask, make_response, jsonify
app = Flask(__name__)

libreOfficeTypes = set(['doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx'])
imageTypes = set(['png', 'jpg', 'jpeg'])    
process = ""
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
            process = subprocess.Popen(command.split())
            return 200
        elif fileType == 'pdf':
            # sudo apt-get install mupdf mupdf-tools
            command = "mupdf /logs/$POD_NAME/" + fileName +' &'
            process = subprocess.Popen(command.split())
            #response = os.system(command)
            return 200
        elif fileType == 'txt':
            # sudo apt install gedit gedit-plugins gedit-common
            command = "gedit /logs/$POD_NAME/" + fileName +' &'
            process = subprocess.Popen(command.split())
            return 200
        elif fileType in imageTypes:
            # sudo apt-get install eog
            command = "eog /logs/$POD_NAME/" + fileName +' &'
            process = subprocess.Popen(command.split())
            return 200
        else:
            response = make_response(jsonify(message="File type not supported"))
            return response, 500
    except:
        e = sys.exc_info()[0]
        return e, 400

@app.route("/file/<fileName>", methods=['DELETE'])
def delete_file(fileName):
    process.terminate()
    os.remove('/logs/$POD_NAME/'+fileName)
    return 200
    

if __name__ == '__main__':
    app.run(host='0.0.0.0')