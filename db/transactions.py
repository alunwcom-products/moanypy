import mariadb
import collections

# Transaction tuple
Transaction = collections.namedtuple('Transaction', 'id, trans_date, entry_date, type, description, comment,'
                                                    'source_type,source_name, source_row, statement_amount, net_amount,'
                                                    'statement_balance, account_balance, account_id, category_id')

PagedTransactions = collections.namedtuple('PagedTransactions', 'total, offset, limit, transactions')

# mapping database columns to Transaction namedtuple
transaction_column_mapping = 'uuid, trans_date, entry_date, type, description, comment, source_type, source_name, ' \
                             'source_row, statement_amount, net_amount, statement_balance, account_balance, account, ' \
                             'category '


def get_transactions(
        conn,
        accounts=None,
        from_date=None,
        to_date=None,
        categories=None,
        text=None,
        offset=0,
        limit=25):

    # construct base SQL query
    query = "FROM transactions "
    first_condition = True
    if accounts:
        query += get_where(first_condition) + "account IN (" + ",".join(f"'{a}'" for a in accounts) + ") "
        first_condition = False
    if from_date:
        query += get_where(first_condition) + "trans_date >= '" + from_date + "' "
        first_condition = False
    if to_date:
        query += get_where(first_condition) + "trans_date <= '" + to_date + "' "
        first_condition = False
    if categories:
        query += get_where(first_condition) + "category IN (" + ",".join(f"'{c}'" for c in categories) + ") "
        first_condition = False
    if text:
        query += get_where(first_condition) + "(description LIKE '%" + text + "%' OR comment LIKE '%" + text + "%') "

    # print(f'query = {query}')

    count = 0
    transactions = []
    try:
        cursor = conn.cursor()
        # get count
        cursor.execute("SELECT count(*) " + query)
        count = next(cursor)[0]
        # get paginated transactions
        cursor.execute("SELECT " + transaction_column_mapping + query +
                       "ORDER BY trans_date DESC LIMIT " + str(offset) + "," + str(limit))
        transactions = list(map(Transaction._make, cursor.fetchall()))

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")

    finally:
        conn.close()

    return PagedTransactions(count, offset, limit, transactions)


# def get_transactions_by_account(conn, account, offset=0, limit=25):
#     count = 0
#     transactions = []
#     try:
#         cursor = conn.cursor()
#         # get count
#         cursor.execute("SELECT count(*) FROM transactions WHERE account = '" + account + "' ")
#         count = next(cursor)[0]
#         # get paginated transactions
#         cursor.execute(
#             "SELECT " + transaction_column_mapping +
#             "FROM transactions "
#             "WHERE account = '" + account + "' "
#             "ORDER BY trans_date ASC, source_row ASC LIMIT " + str(offset) + "," + str(limit))
#         transactions = list(map(Transaction._make, cursor.fetchall()))
#
#     except mariadb.Error as e:
#         print(f"Error connecting to MariaDB Platform: {e}")
#
#     finally:
#         conn.close()
#
#     return PagedTransactions(count, offset, limit, transactions)


def get_where(is_first):
    if is_first:
        return "WHERE "
    else:
        return "AND "
