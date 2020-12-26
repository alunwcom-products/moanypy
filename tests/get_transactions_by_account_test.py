import db

if __name__ == "__main__":
    db.database_connection(
        database="moany",
        user="moany",
        password="password"
    )

    accounts = db.get_accounts(db.get_connection())
    for account in accounts:
        transactions = db.get_transactions_by_account(db.get_connection(), account['uuid'])
        print(f'Account: {account["name"]}, total transactions = {len(transactions)}')

        display_count = 5
        if len(transactions) < display_count:
            display_count = len(transactions)

        for i in range(display_count):
            print(transactions[i])

        print(' ')
