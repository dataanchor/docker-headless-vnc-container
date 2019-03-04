#!/usr/bin/env bash
### every exit != 0 fails the script
set -e

echo "Install sftp"
apt-get update 
apt-get install -y vsftpd
mkdir $HOME/sftp
chown 1000:0 $HOME/sftp
chmod 777 $HOME/sftp
cp /etc/vsftpd.conf /etc/vsftpd.conf.orig
service vsftpd start &
apt install -y openssh-server
apt-get clean -y

echo "running python script"
python $STARTUPDIR/watch-files.py $HOME/sftp &