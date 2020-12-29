import mariadb
import collections

# Transaction tuple
Transaction = collections.namedtuple('Transaction', 'id, trans_date, entry_date, type, description, source_type,'
                                                    'source_name, source_row, statement_amount, net_amount,'
                                                    'statement_balance, account_balance, account_id')

PagedTransactions = collections.namedtuple('PagedTransactions', 'total, offset, limit, transactions')

# mapping database columns to Transaction namedtuple
transaction_column_mapping = 'uuid, trans_date, entry_date, type, description, source_type, source_name, source_row, ' \
                         'statement_amount, net_amount, statement_balance, account_balance, account '


def get_transactions(conn, offset=0, limit=25):
    count = 0
    transactions = []
    try:
        cursor = conn.cursor()
        # get count
        cursor.execute("SELECT count(*) FROM transactions")
        count = next(cursor)[0]
        # get paginated transactions
        cursor.execute("SELECT " + transaction_column_mapping +
                       "FROM transactions ORDER BY trans_date DESC LIMIT " + str(offset) + "," + str(limit))
        transactions = list(map(Transaction._make, cursor.fetchall()))

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")

    finally:
        conn.close()

    return PagedTransactions(count, offset, limit, transactions)


def get_transactions_by_account(conn, account, offset=0, limit=25):
    count = 0
    transactions = []
    try:
        cursor = conn.cursor()
        # get count
        cursor.execute("SELECT count(*) FROM transactions WHERE account = '" + account + "' ")
        count = next(cursor)[0]
        # get paginated transactions
        cursor.execute(
            "SELECT " + transaction_column_mapping +
            "FROM transactions "
            "WHERE account = '" + account + "' "
            "ORDER BY trans_date ASC, source_row ASC LIMIT " + str(offset) + "," + str(limit))
        transactions = list(map(Transaction._make, cursor.fetchall()))

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")

    finally:
        conn.close()

    return PagedTransactions(count, offset, limit, transactions)
