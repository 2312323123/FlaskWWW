import mysql.connector

connection = mysql.connector.connect(user='root', password='Mocne_haslo123', host='127.0.0.1',
                                     database='for_project', auth_plugin='mysql_native_password')
query = 'SELECT * FROM users'

cursor = connection.cursor()
cursor.execute(query)
for row in cursor:
    print(row)

connection.close()

