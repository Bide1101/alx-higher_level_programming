-- This script lists the privileges of MySQL users user_0d_1 and user_0d_2
mysql -u root -p
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
