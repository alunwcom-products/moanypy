import mariadb


def get_transaction(conn):
    transactions = []
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT trans_date, description FROM transactions ORDER BY trans_date DESC")
        for (trans_date, description) in cursor:
            transactions.append(f"{trans_date} {description}")

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")

    finally:
        conn.close()

    return transactions
