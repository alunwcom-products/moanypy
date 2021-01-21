import collections

import mysql.connector

# Account tuple
# Account = collections.namedtuple('Account', 'id, number, name, type, starting_balance')

# mapping database columns to Account namedtuple
account_column_mapping = 'uuid, account_num, name, type, starting_balance '


def get_accounts(conn):
    """
    Get (all) accounts - ordered by name ascending.

    :param conn:
    :return: list of Account tuples
    """
    accounts = []
    try:
        cursor = conn.cursor(named_tuple=True)
        cursor.execute(
            "SELECT " +
            account_column_mapping +
            "FROM accounts ORDER BY name ASC")

        accounts = cursor.fetchall()

    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")

    finally:
        conn.close()

    return accounts
