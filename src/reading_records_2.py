from getpass import getpass
from mysql.connector import connect, Error


try:
    # Establishing a connection with MySQL
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=getpass("Enter password: "),
        database="online_movie_rating",
    ) as connection:
        # Reading records
        select_movies_query = "SELECT title, release_year FROM movies LIMIT 3"
        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            for row in cursor.fetchall():
                print(row)
except Error as e:
    print(e)
