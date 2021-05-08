from getpass import getpass
from mysql.connector import connect, Error

# Establishing a connection with MySQL
try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="online_movie_rating",
    ) as connection:
        drop_table_query = "DROP TABLE ratings"
        with connection.cursor() as cursor:
            cursor.execute(drop_table_query)
            print("Table ratings")
except Error as e:
    print(e)
