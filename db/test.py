import mariadb
import sys


if __name__ == "__main__":
    try:
        # Instantiate Connection
        conn = mariadb.connect(
            user="moany",
            password="password",
            host="localhost",
            port=3306)

        # Instantiate Cursor
        cur = conn.cursor()

        # Initialize Variables
        transactions = []

        # Retrieve Contacts
        cur.execute("SELECT trans_date, description FROM moany.transactions ORDER BY trans_date DESC LIMIT 0,25")

        # Prepare Contacts
        for (trans_date, description) in cur:
            transactions.append(f"{trans_date} {description}")

        # List Contacts
        print("\n".join(transactions))

        # Close Connection
        conn.close()

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
