import db

if __name__ == "__main__":
    db.database_connection(
        database="moany",
        user="moany",
        password="password"
    )

    accounts = db.get_accounts(db.get_connection())
    for account in accounts:
        results = db.get_transactions_by_account(db.get_connection(), account.id, 0, 5)
        print(f'Account: {account.name}, total transactions = {len(results.transactions)}')

        # for t in results.transactions:
        #     print(t)

        total_amount = 0
        balance = 0
        for i, t in enumerate(results.transactions):
            if i == 0:
                balance = t.account_balance
            else:
                balance += t.net_amount

            total_amount += t.net_amount
            # print(f'{t}')
            print(
                f'{t.trans_date} [{t.source_row}] {t.net_amount:>9} {balance:>9} [{t.account_balance:>9}]')

        print(f'Sub-total = {total_amount}')
        print(' ')
