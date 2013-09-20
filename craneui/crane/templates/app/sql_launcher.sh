#!/bin/bash
/usr/bin/mysql_install_db ; # --datadir='/home/qa/databases';
/usr/sbin/mysqld & # --datadir='/home/qa/databases' &

echo '------------------------------ MYSQLD LAUNCHED'
sleep 5;

mysql --user=root --execute=\
" UPDATE mysql.user SET Password = PASSWORD('toor')
     WHERE User = 'root';
 FLUSH PRIVILEGES;
";

mysql --user=root --password="toor" --execute="CREATE DATABASE test;";
mysql --user=root --password="toor" --execute="DROP USER ''@'localhost';";
mysql --user=root --password="toor" --execute="CREATE USER 'qa'@'%' IDENTIFIED BY 'aq';"
mysql --user=root --password="toor" --execute="GRANT ALL PRIVILEGES ON *.* TO 'qa'@'%' IDENTIFIED BY 'aq';"
echo '------------------------------ MYSQLD CONFIGURED'
