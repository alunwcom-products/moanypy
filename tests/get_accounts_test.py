import db

if __name__ == "__main__":
    db.database_connection(
        database="moany",
        user="moany",
        password="password"
    )
    results = db.get_accounts(db.get_connection())

    for account in results:
        print(account)

    print(f'count = {len(results)}')