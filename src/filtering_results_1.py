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
        # Filtering results
        select_movies_query = """
        SELECT CONCAT(title, " (", release_year, ")"), rate
        FROM movies
        ORDER BY rate DESC
        """
        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            for movie in cursor.fetchall():
                print(movie)
except Error as e:
    print(e)
