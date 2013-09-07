#!/bin/bash

# Launch sshd
/usr/sbin/sshd;

cd `dirname "$0"`;
rbenv rehash;

# Launch the app in background

{{launch}} &

# After launch
{% if after_launch %}
{{after_launch}}
{% else %}
while true; do
    sleep 60;
done
{% endif %}
