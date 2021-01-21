import mysql.connector


if __name__ == "__main__":
    try:

        dbconfig = {
            "database": "moany",
            "user": "moany",
            "password": "password"
        }
        connection = mysql.connector.connect(
            pool_name="my_pool",
            pool_size=3,
            **dbconfig
        )

        # connection = mysql.connector.connect(
        #     host="localhost",
        #     user="moany",
        #     database="moany",
        #     password="password",
        # )

        select_movies_query = "SELECT * FROM accounts"
        with connection.cursor(named_tuple=True) as cursor:
            cursor.execute(select_movies_query)
            # result = cursor.fetchall()
            for row in cursor:
                print(f'{row.name} {row.starting_balance}')

        conn2 = mysql.connector.connect(pool_name="my_pool")
        cursor2 = conn2.cursor(named_tuple=True)
        cursor2.execute(select_movies_query)
        for row in cursor2:
            print(row)

    except mysql.connector.Error as e:
        print(e)
