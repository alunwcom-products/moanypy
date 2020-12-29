import db

if __name__ == "__main__":
    db.database_connection(
        database="moany",
        user="moany",
        password="password"
    )
    results = db.get_accounts(db.get_connection())

    for account in results:
        print(f'{account.id:<36} | {account.number:<20} | {account.name:<20} | {account.type:<6} | {account.starting_balance:>10}')

    print(f'count = {len(results)}')