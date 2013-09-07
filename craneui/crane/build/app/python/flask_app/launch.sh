#!/bin/bash

# Launch sshd
/usr/sbin/sshd;

cd `dirname "$0"`;
source venv/bin/activate;

# Launch the app in background

python app.py &

# After launch

while true; do
    sleep 60;
done
