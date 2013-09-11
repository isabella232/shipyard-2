#!/bin/bash

# Launch sshd
/usr/sbin/sshd;

/etc/init.d/postgresql start;

sudo -u postgres psql -U postgres -d postgres -c "alter user postgres with password '{{password}}';";

while true; do
    sleep 60;
done
