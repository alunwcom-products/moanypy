import db

if __name__ == "__main__":
    db.database_connection(
        database="moany",
        user="moany",
        password="password"
    )

    results = db.get_transactions(db.get_connection())

    # list first 5 transactions
    for i in range(5):
        print(results[i])

    print(f'count = {len(results)}')
