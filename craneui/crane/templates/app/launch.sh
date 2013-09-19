#!/bin/bash

# This function is used to concatenate the parameters.
# Due to docker py limitations we cannot pass them as one string
# to the shell and eval it.
function concatenate_args
{
    string=""
    for a in "$@" # Loop over arguments
    do
        if [[ "$string" != "" ]]
        then
            string+=" " # Delimeter
        fi
        string+="$a"
    done
    echo "$string"
}

/usr/bin/mysql_install_db --datadir='/home/qa/databases';
/usr/sbin/mysqld --datadir='/home/qa/databases' &

sleep 10;

mysql --user=root --execute=\
" UPDATE mysql.user SET Password = PASSWORD('toor')
     WHERE User = 'root';
 FLUSH PRIVILEGES;
";

mysql --user=root --password="toor" --execute="DROP USER ''@'localhost';";
mysql --user=root --password="toor" --execute="DROP DATABASE test";
mysql --user=root --password="toor" --execute="CREATE USER 'qa'@'%' IDENTIFIED BY 'aq';"
mysql --user=root --password="toor" --execute="GRANT ALL PRIVILEGES ON *.* TO 'qa'@'%' IDENTIFIED BY 'aq';"

cd `dirname "$0"`;
{{env_manager}};

command="$(concatenate_args "$@")";

if [ $# -eq 0 ]  || [[ $# -gt 0  &&  -z "$command" ]]
then
	# Launch the app in background
	{{launch}} &
else
	eval "$command" &
fi

# After launch
{% if after_launch %}
{{after_launch}}
{% endif %}
