#!/bin/bash

# Launch sshd
/usr/sbin/sshd;

sudo -u qa ./launch.sh;

while true; do
    sleep 60;
done
