import db

if __name__ == "__main__":
    db.database_connection(
        database="moany",
        user="moany",
        password="password"
    )

    results = db.get_transactions(db.get_connection(), 0)

    for t in results:
        print(t)

    print(f'results = {len(results)}')
