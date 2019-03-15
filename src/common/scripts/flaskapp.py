import os
import subprocess
import sys
import signal
from flask import Flask, make_response, jsonify
import logging
app = Flask(__name__)

libreOfficeTypes = set(['doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx'])
imageTypes = set(['png', 'jpg', 'jpeg'])    
process = ""
@app.route("/")
def hello():
    return "hello"

@app.route("/file/<fileName>")
def open_file(fileName):
    global process
    if '.' in fileName:
        fileType = fileName.rsplit('.', 1)[1].lower()
    try:
        filePath = '/logs/'+os.environ['HOSTNAME']+'/'+fileName
        logging.info("file path generated %s", filePath)
        print filePath
        if fileType in libreOfficeTypes:
            # sudo apt-get install libreoffice
            command = "libreoffice " + filePath + ' &'
            global process
            process = subprocess.Popen(command.split())
            return str(process.pid)
        elif fileType == 'pdf':
            # sudo apt-get install mupdf mupdf-tools
            command = "mupdf " + filePath +' &'
            global process
            process = subprocess.Popen(command.split())
            #response = os.system(command)
            return str(process.pid)
        elif fileType == 'txt':
            # sudo apt install gedit gedit-plugins gedit-common
            command = "gedit " + filePath +' &'
            logging.info("came to txt %s", command)
            global process
            process = subprocess.Popen(command.split())
            return str(process.pid)
        elif fileType in imageTypes:
            # sudo apt-get install eog
            command = "eog " + filePath +' &'
            global process
            process = subprocess.Popen(command.split())
            return str(process.pid)
        else:
            response = make_response(jsonify(message="File type not supported"))
            return response, 500
    except:
        logging.warning("error %s", e)
        e = sys.exc_info()[0]
        return e, 400

@app.route("/file/<fileName>/<pid>", methods=['DELETE'])
def delete_file(fileName,pid):
    os.kill(pid,signal.SIGKILL)
    filePath = '/logs/'+os.environ['HOSTNAME']+'/'+fileName
    os.remove(filePath)
    return 'deleted file'
    

if __name__ == '__main__':
    logging.basicConfig(filename = "DAtAnchorFlaskApp.log", format = '%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level = logging.DEBUG)
    app.run(host='0.0.0.0')