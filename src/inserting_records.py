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
        # Inserting records in table
        insert_movies_query = """
        INSERT INTO movies (title, release_year, genre, rate)
        VALUES
            ("Matrix", 1999, "Sci-Fi", 8.7),
            ("Seven: The Seven Capital Crimes", 1995, "Crime", 8.6),
            ("The GodFather", 1972, "Crime", 9.2),
            ("The Shawshank Redemption", 1994, "Drama", 9.3),
            ("Casablanca", 1942, "War", 8.5),
            ("Citizen Kane", 1941, "Mystery", 8.3),
            ("Gone With the Wind", 1939, "Romance", 8.1),
            ("Lawrence of Arabia", 1962, "Adventure", 8.3),
            ("The Sound of Music", 1965, "Biography", 8.0),
            ("The Silence of the Lambs", 1991, "Crime", 8.6)
        """
        with connection.cursor() as cursor:
            cursor.execute(insert_movies_query)
            connection.commit()
except Error as e:
    print(e)
