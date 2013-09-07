#!/bin/bash

# Launch sshd
/usr/sbin/sshd;

cd `dirname "$0"`;
rbenv rehash;

# Launch the app in background

ruby app.rb &

# After launch

while true; do
    sleep 60;
done
