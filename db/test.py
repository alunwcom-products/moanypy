import mariadb


# Create Connection Pool
def create_connection_pool():
    """Creates and returns a Connection Pool"""

    # Create Connection Pool
    _pool = mariadb.ConnectionPool(
        database="moany",
        user="moany",
        password="password",
        host="localhost",
        port=3306,
        autocommit=False,
        pool_name="web-app",
        pool_size=20
    )

    # Return Connection Pool
    return _pool


# Adds account
def add_transaction(_cur, _uuid):
    print(f'uuid = {_uuid}')
    _cur.execute("INSERT INTO transactions(uuid, account) VALUES (?, ?)", (_uuid, "none"))


# Remove Contact from Database
def remove_transactions_by_account(_cur, _account):
    cur.execute("DELETE FROM transactions WHERE account = ?", (_account,))


if __name__ == "__main__":
    try:

        pool = create_connection_pool()
        conn = pool.get_connection()

        # Instantiate Cursor
        cur = conn.cursor()

        # Initialize Variables
        transactions = []

        # Retrieve Contacts
        cur.execute(
            "SELECT "
            "uuid, "
            "statement_amount, "
            "description, "
            "comment, "
            "entry_date, "
            "source_name, "
            "source_row, "
            "source_type "
            "FROM transactions ORDER BY entry_date DESC")

        # Prepare Contacts
        for (row) in cur:
            # transactions.append(f"{row[0]} {row[4]} {row[7]}")
            timestamp = row[4]
            if timestamp:
                print(f'date = {timestamp.strftime("%b %d %Y %H:%M:%S")}')

        # List Contacts
        # print("\n".join(transactions))

        # add_transaction(cur, str(uuid.uuid4()))

        # remove_transactions_by_account(cur, "none")

        conn.commit()

        # Close Connection
        conn.close()

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")

        conn.rollback()

        # sys.exit(1)
