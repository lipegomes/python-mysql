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
        alter_table_query = """
        ALTER TABLE movies
        MODIFY COLUMN collection_in_mil DECIMAL(4,1)
        """
        show_table_query = "DESCRIBE movies"
        with connection.cursor() as cursor:
            cursor.execute(alter_table_query)
            cursor.execute(show_table_query)
            # Fetch rows from last executed query
            result = cursor.fetchall()
            print("Movie Table Schme after alteration:")
            for row in result:
                print(row)
except Error as e:
    print(e)
