import mariadb

# mapping database columns to property names
std_columns = {
    'uuid': 'id',
    'account_num': 'number',
    'name': 'name',
    'type': 'type',
    'starting_balance': 'starting_balance'
}


def get_accounts(conn):
    accounts = []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT " + ",".join(std_columns.keys()) + " FROM accounts ORDER BY name ASC")
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]

        for (row) in cursor:
            account = {}
            for i in range(num_fields):
                account[std_columns[field_names[i]]] = row[i]
            accounts.append(account)

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")

    finally:
        conn.close()

    return accounts
