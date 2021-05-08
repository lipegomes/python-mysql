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
        # Updating Database
        update_query = """
        UPDATE
            reviewers
        SET
            last_name = "Cooper"
        WHERE;

        UPDATE
            reviewers
        SET
            last_name = "Cannavi"
        WHERE
            first_name = "Thomas";

        UPDATE
            reviewers
        SET
            last_name = "Buzeer"
        WHERE
            first_name = "Sheldon;

        UPDATE
            reviewers
        SET
            last_name = "Cat"
        WHERE
            first_name = "Kat";

        UPDATE
            reviewers
        SET
            last_name = "Vargas"
        WHERE
            first_name = "Andre";

        UPDATE
            reviewers
        SET
            last_name = "Legal"
        WHERE
            first_name = "Domingo";
        """

        with connection.cursor() as cursor:
            for result in cursor.execute(update_query, multi=True):
                if result.with_rows:
                    print(result.fetchall())
            connection.commit()
            print("Update of completed queries.")
except Error as e:
    print(e)
