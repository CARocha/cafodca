#!/bin/bash

DBNAME=database
PASSWORD=very-bad-password

# Some of the datetime data in the old MyISAM tables were giving
# InnoDB a rough time so here they are updated to something InnoDB
# feels more comfortable with. Subqueries didn't work and I
# couldn't be bothered to figure out why.
IDS=$(mysql "$DBNAME" -u root -p"$PASSWORD" -e "SELECT id FROM appname_modelname WHERE timestamp_created = '0000-00-00 00:00:00';")
for ROW_ID in $IDS; do
    mysql "$DBNAME" -u root -p"$PASSWORD" -e "UPDATE appname_modelname SET timestamp_created = '0001-01-01 00:00:00' WHERE id = $ROW_ID";
    echo $ROW_ID
done

mysql "$DBNAME" -u root -p"$PASSWORD" -e "SHOW TABLE STATUS WHERE ENGINE = 'MyISAM';" | awk 'NR>1 {print "ALTER TABLE "$1" ENGINE = InnoDB;"}' | mysql -u root -p"$PASSWORD" "$DBNAME"
