#!/bin/sh

# mysql -h host_name -P 3306 -u db_master_user -p
# mysql -u usr -p '-e source file_path.sql'
# source db.sql
mysql -h utopiards.cs32qiajmyjf.us-east-1.rds.amazonaws.com -P 3306 -u "utopia" -p "utopiacoolpassword" utopia < db.baby.sql