import mariadb
import uuid


# Create Connection Pool
def create_connection_pool():
    """Creates and returns a Connection Pool"""

    # Create Connection Pool
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

    # Return Connection Pool
    return pool


# Adds account
def add_account(_cur, _uuid):
    """
    Adds the given account to the accounts table
    """

    print(f'uuid = {_uuid}')
    _cur.execute("INSERT INTO transactions(uuid, account) VALUES (?, ?)", (_uuid, "none"))


if __name__ == "__main__":
    try:
        # Instantiate Connection
        # conn = mariadb.connect(
        #     database="moany",
        #     user="moany",
        #     password="password",
        #     host="localhost",
        #     port=3306,
        #     autocommit=False)

        pool = create_connection_pool()
        conn = pool.get_connection()

        # Instantiate Cursor
        cur = conn.cursor()

        # Initialize Variables
        transactions = []

        # Retrieve Contacts
        cur.execute("SELECT trans_date, description FROM transactions ORDER BY trans_date DESC LIMIT 0,25")

        # Prepare Contacts
        for (trans_date, description) in cur:
            transactions.append(f"{trans_date} {description}")

        # List Contacts
        print("\n".join(transactions))

        add_account(cur, str(uuid.uuid4()))

        conn.commit()

        # Close Connection
        conn.close()

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        conn.rollback()

        # sys.exit(1)
