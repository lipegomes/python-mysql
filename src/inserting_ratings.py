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
        # Inserting ratings in table
        insert_ratings_query = """
        INSERT INTO ratings
        (rating, movie_id, reviewer_id)
        VALUES ( %s, %s, %s)
        """
        ratings_records = [
            (8.7, 1, 5), (8.6, 2, 1), (9.2, 3, 14), (9.3, 4, 17),
            (8.5, 5, 8), (8.5, 6, 5), (8.1, 7, 13), (8.3, 8, 11),
            (8.0, 9, 4), (8.6, 10, 1)
        ]
        with connection.cursor() as cursor:
            cursor.executemany(insert_ratings_query, ratings_records)
            connection.commit()

except Error as e:
    print(e)
