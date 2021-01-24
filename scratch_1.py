import mysql.connector
import os


if __name__ == "__main__":

    moany_password = os.environ['MOANY_PASSWORD']
    print("Testing...")

    try:
        dbconfig = {
            "database": "moany",
            "user": "moany",
            "password": moany_password
        }
        connection = mysql.connector.connect(
            pool_name="moany_pool",
            pool_size=3,
            database="moany",
            user="moany",
            password=moany_password,
            host="localhost",
            port="3306",
            autocommit=False
        )
        conn = mysql.connector.connect(pool_name="moany_pool")
        cursor = conn.cursor(named_tuple=True)
        cursor.execute(
            "SELECT * FROM transactions ORDER BY trans_date DESC LIMIT 0,10")
            # "SELECT * FROM accounts ORDER BY name ASC")

        accounts = cursor.fetchall()
        for a in accounts:
            print(f'{a}')

    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")

