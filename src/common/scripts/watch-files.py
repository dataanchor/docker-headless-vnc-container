import os
import sys
import time
import logging
import mimetypes
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import PatternMatchingEventHandler

# Event Handler for the Observer thread
class CustomEventHandler(PatternMatchingEventHandler):
    patterns = ["*.txt", "*.pdf", "*.doc", 
                "*.ppt", "*.docx", "*.pptx",
                "*.jpg", "*.jpeg", "*.png"]

    def executeSystemCommand(self, command):
        try:
            response = os.system(command)
            if response == 0:
                logging.info("Shell command execution successful: %s", command)
            else:
                logging.warning("Shell command execution failed: %s", command)
        except:
            e = sys.exc_info()[0]
            logging.warning("Shell command execution throwned an exception: %s", e)

    def process(self, event):
        """
        event.event_type 
            'modified' | 'created'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        if event.is_directory:
            return None
        
        file_type = str((mimetypes.guess_type(event.src_path))[0])
        logging.info("New file created with file type %s: ", file_type)
        # os.system("export DISPLAY=:1")

        if (file_type == "text/plain" or file_type == "image/jpeg" or file_type == "image/jpg"
            or file_type == "image/png" or file_type == "application/pdf"):
            # TODO: Change this command based on file type. gedit for text files
            command = "google-chrome " + event.src_path
            self.executeSystemCommand(command)
        elif (file_type == "application/msword" or file_type == "application/vnd.openxmlformats-officedocument.presentationml.presentation"):
            # TODO: Change this command based on file type. Libre for doc, docx files
            # command = "open -a 'Google Chrome' " + event.src_path
            # self.executeSystemCommand(command)
            logging.info("Just logging because its a doc or docx document")
        elif (file_type == "application/vnd.openxmlformats-officedocument.presentationml.presentation"):
            # TODO: Change this command based on file type. Libre for ppt, pptx files
            # command = "open -a 'Google Chrome' " + event.src_path
            # self.executeSystemCommand(command)
            logging.info("Just logging because its a doc or docx document")
        else:
            logging.info("Unsupported file type %s: ", file_type)

    def on_modified(self, event):
        print "Modified: " + event.src_path + "\n"
        # self.process(event)

    def on_created(self, event):
        self.process(event)

class Watcher:
    def __init__(self, path):
        self.observer = Observer()
        self.path = path

    def run(self):
        event_handler = CustomEventHandler()
        self.observer.schedule(event_handler, self.path, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            e = sys.exc_info()[0]
            self.observer.stop()
            logging.warning("Watchdog failed with exception %s", e)

        self.observer.join()

if __name__ == '__main__':
    logging.basicConfig(filename = "DAtAnchorWatchdog.log", format = '%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level = logging.DEBUG)
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    w = Watcher(path)
    w.run() 

# File System Event Handler Class
# class Handler(FileSystemEventHandler):

#     @staticmethod
#     def on_any_event(event):
#         if event.is_directory:
#             return None

#         elif event.event_type == 'created':
#             # Take any action here when a file is first created.
#             print "Received created event - %s." % event.src_path
#             command = "code " + event.src_path
#             os.system("export DISPLAY")
#             os.system(command)

#         elif event.event_type == 'modified':
#             # Taken any action here when a file is modified.
#             print "Received modified event - %s." % event.src_path