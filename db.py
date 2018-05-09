# -*-coding: utf-*-

import pymysql as mariadb

mariadb_connection = mariadb.connect(user='root', password='511', database='')
cursor = mariadb_connection.cursor()

#insert information
some_id = 4
is_admin = 0
try:
    cursor.execute("INSERT INTO USER (user_id, admin) VALUE (%s, %s)", (some_id, is_admin))
except mariadb.Error as error:
    print ("Error: {}".format(error))

#retrieving information
cursor.execute("SELECT user_id, admin FROM USER WHERE user_id=%s", (some_id,))
for user_id, admin in cursor:
    print ("USER ID: {}, ADMIN: {}".format(user_id, admin))

mariadb_connection.commit()
if is_admin == 1:
    autority = "Administrator"
else:
    autority = "User"
print ("The last inserted USRE ID was: {}, His autority is: {} ".format(some_id, autority))