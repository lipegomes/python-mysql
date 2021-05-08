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
        # Select query
        select_movies_query = """
        SELECT reviewer_id, movie_id FROM ratings
        WHERE reviewer_id = 5
        """
        # Delete query
        delete_query = "DELETE FROM ratings WHERE reviewer_id = 5"

        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            for movie in cursor.fetchall():
                print(f"Movie: {movie}")
            cursor.execute(delete_query)
            connection.commit()
            print("Deleted queries.")
except Error as e:
    print(e)
