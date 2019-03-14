#!/usr/bin/env bash
### every exit != 0 fails the script
set -e

echo "Install sftp"
apt-get update 
apt-get install -y inotify-tools
mkdir $HOME/sftp
chown 1000:0 $HOME/sftp
chmod 777 $HOME/sftp
apt-get install -y curl
apt-get install -y mupdf mupdf-tools
apt-get install -y eog
apt-get clean -y

echo "running python script"
# python $STARTUPDIR/watch-files.py /logs/$POD_NAME &