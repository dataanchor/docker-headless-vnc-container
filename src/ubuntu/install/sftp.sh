#!/usr/bin/env bash
### every exit != 0 fails the script
set -e

echo "Install sftp"
apt-get update 
apt-get install vsftpd
cp /etc/vsftpd.conf /etc/vsftpd.conf.orig
apt-get clean -y
