#!/bin/bash

# Launch sshd
/usr/sbin/sshd;

cd `dirname "$0"`;
sudo -u qa ./launch.sh $1;

while true; do
    sleep 60;
done
