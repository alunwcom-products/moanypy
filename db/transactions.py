import mariadb

pool = mariadb.ConnectionPool(
    database="moany",
    user="moany",
    password="password",
    host="localhost",
    port=3306,
    autocommit=False,
    pool_name="web-app",
    pool_size=20
)


def get_transaction():
    transactions = []
    try:
        conn = pool.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT trans_date, description FROM transactions ORDER BY trans_date DESC LIMIT 0,25")
        for (trans_date, description) in cursor:
            transactions.append(f"{trans_date} {description}")

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")

    finally:
        conn.close()

    return transactions
