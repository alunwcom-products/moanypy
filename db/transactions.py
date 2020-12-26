import mariadb

std_columns = [
    'uuid',
    'trans_date',
    'entry_date',
    'type',
    'description',
    'source_type',
    'source_name',
    'source_row',
    'statement_amount',
    'net_amount',
    'statement_balance',
    'account_balance',
    'account'
]


def get_transactions(conn):
    transactions = []
    try:
        cursor = conn.cursor()

        std_columns = [
            'uuid',
            'trans_date',
            'entry_date',
            'type',
            'description',
            'source_type',
            'source_name',
            'source_row',
            'statement_amount',
            'net_amount',
            'statement_balance',
            'account_balance',
            'account'
        ]
        cursor.execute("SELECT " + ",".join(std_columns) + " FROM transactions ORDER BY trans_date DESC")
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]

        for (row) in cursor:
            transaction = {}
            for i in range(num_fields):
                transaction[field_names[i]] = row[i]
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
            "SELECT " + ",".join(std_columns) + " FROM transactions "
            "WHERE account = '" + account + "' "
            "ORDER BY trans_date DESC")
        num_fields = len(cursor.description)
        field_names = [i[0] for i in cursor.description]

        for (row) in cursor:
            transaction = {}
            for i in range(num_fields):
                transaction[field_names[i]] = row[i]
            transactions.append(transaction)

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")

    finally:
        conn.close()

    return transactions
