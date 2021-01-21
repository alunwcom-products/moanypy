import pymysql.cursors


if __name__ == "__main__":
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='moany',
                                 password='password',
                                 database='moany',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection:
        # with connection.cursor() as cursor:
        #     # Create a new record
        #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        #
        # # connection is not autocommit by default. So you must commit to save
        # # your changes.
        # connection.commit()

        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM accounts"
            cursor.execute(sql)

            for row in cursor.fetchall():
                print(row['uuid'])
