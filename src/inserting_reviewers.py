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
        # Inserting reviewers in table
        insert_reviewers_query = """
        INSERT INTO reviewers
        (first_name, last_name)
        VALUES ( %s, %s )
        """
        reviewers_records = [
            ("Chaitanya", "Baweja"),
            ("Mary", "Cooper"),
            ("John", "Wayne"),
            ("Thomas", "Stoneman"),
            ("Penny", "Hofstadter"),
            ("Mitchell", "Marsh"),
            ("Wyatt", "Skaggs"),
            ("Andre", "Veiga"),
            ("Sheldon", "Cooper"),
            ("Kimbra", "Masters"),
            ("Kat", "Dennings"),
            ("Bruce", "Wayne"),
            ("Domingo", "Cortes"),
            ("Rajesh", "Koothrappali"),
            ("Ben", "Glocker"),
            ("Mahinder", "Dhoni"),
            ("Akbar", "Khan"),
            ("Howard", "Wolowitz"),
            ("Pinkie", "Petit"),
            ("Gurkaran", "Singh"),
            ("Amy", "Farah Fowler"),
            ("Marlon", "Crafford"),
        ]
        with connection.cursor() as cursor:
            cursor.executemany(insert_reviewers_query, reviewers_records)
            connection.commit()

except Error as e:
    print(e)
