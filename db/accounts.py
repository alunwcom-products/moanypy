import mariadb


def get_accounts(conn):
    accounts = []
    try:
        cursor = conn.cursor()

        std_columns = [
            'uuid',
            'account_num',
            'name',
            'type',
            'starting_balance'
        ]
        cursor.execute("SELECT " + ",".join(std_columns) + " FROM accounts ORDER BY name ASC")
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]

        for (row) in cursor:
            account = {}
            for i in range(num_fields):
                account[field_names[i]] = row[i]
            accounts.append(account)

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")

    finally:
        conn.close()

    return accounts
