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
        # Handling Multiple
        select_movies_query = """
        SELECT CONCAT(first_name, " ", last_name), COUNT(*) as num
        FROM reviewers
        INNER JOIN ratings
            ON reviewers.id = ratings.reviewer_id
        GROUP BY reviewer_id
        ORDER BY num DESC
        LIMIT 1
        """
        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            for movie in cursor.fetchall():
                print(movie)
except Error as e:
    print(e)
