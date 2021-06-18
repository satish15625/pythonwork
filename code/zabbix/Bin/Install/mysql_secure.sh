#!/bin/bash

yum -y install expect

# // Not required in actual script
# MYSQL_ROOT_PASSWORD=%LdNB>dHo6h+


SECURE_MYSQL=$(expect -c "
set timeout 10
spawn mysql_secure_installation
expect \"Enter password for user root:\"
send \"$1\r\"
expect \"The existing password for the user account root has expired. Please set a new password.
		New password:\"
send \"$2\r\"
expect \"Re-enter new password:\"
send \"$2\r\"
expect \"Change the password for root ? (Press y|Y for Yes, any other key for No) :\"
send \"n\r\"
expect \"Remove anonymous users? (Press y|Y for Yes, any other key for No) :\"
send \"y\r\"
expect \"Disallow root login remotely? (Press y|Y for Yes, any other key for No) :\"
send \"n\r\"
expect \"Remove test database and access to it? (Press y|Y for Yes, any other key for No) :\"
send \"y\r\"
expect \"Reload privilege tables now? (Press y|Y for Yes, any other key for No) :\"
send \"y\r\"
expect eof
")

echo "$SECURE_MYSQL"

# yum -y purge expect