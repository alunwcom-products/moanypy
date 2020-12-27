import mariadb

std_columns = {
    'uuid': 'id',
    'trans_date': 'trans_date',
    'entry_date': 'entry_date',
    'type': 'type',
    'description': 'description',
    'source_type': 'source_type',
    'source_name': 'source_name',
    'source_row': 'source_row',
    'statement_amount': 'statement_amount',
    'net_amount': 'net_amount',
    'statement_balance': 'statement_balance',
    'account_balance': 'account_balance',
    'account': 'account_id'
}


def get_transactions(conn, offset=0, limit=25):
    transactions = []
    try:
        cursor = conn.cursor()
        # get count
        cursor.execute("SELECT count(*) FROM transactions")
        count = next(cursor)[0]
        print(f'count = {count}')

        cursor.execute("SELECT " + ",".join(std_columns.keys()) + " FROM transactions ORDER BY trans_date DESC LIMIT " + str(offset) + "," + str(limit))
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]

        for (row) in cursor:
            transaction = {}
            for i in range(num_fields):
                transaction[std_columns[field_names[i]]] = row[i]
            transactions.append(transaction)

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")

    finally:
        conn.close()

    return transactions


def get_transactions_by_account(conn, account):
    transactions = []
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT " + ",".join(std_columns.keys()) + " FROM transactions "
            "WHERE account = '" + account + "' "
            "ORDER BY trans_date DESC")
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]

        for (row) in cursor:
            transaction = {}
            for i in range(num_fields):
                transaction[std_columns[field_names[i]]] = row[i]
            transactions.append(transaction)

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")

    finally:
        conn.close()

    return transactions
