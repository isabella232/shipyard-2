#!/bin/bash

# Launch sshd
/usr/sbin/sshd;

{{launch}}

# After launch
{% if after_launch %}
{{after_launch}}
{% else %}
while true; do
    sleep 60;
done
{% endif %}
