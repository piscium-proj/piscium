# -*-coding: utf-*-

import pymysql as mariadb
from config import mariadb_option

mariadb_connection = mariadb.connect(**mariadb_option)
cursor = mariadb_connection.cursor()

#insert information
'''
some_id = 3
try:
    cursor.execute("INSERT INTO pis_user (user_id, user_admin) VALUE (%s, %s)", (some_id, 1))
except mariadb.Error as error:
    print ("Error: {}".format(error))

#retrieving information
cursor.execute("SELECT user_id, user_admin FROM pis_user WHERE user_id=%s", (some_id,))
for user_id, user_admin in cursor:
    print ("USER ID: {}, ADMIN: {}".format(user_id, user_admin))

mariadb_connection.commit()
if user_admin == 1:
    autority = "Administrator"
else:
    autority = "User"
print ("The last inserted USRE ID was: {}, His autority is: {} ".format(some_id, autority))
'''

