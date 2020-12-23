import db

if __name__ == "__main__":
    db.database_connection(
        database="moany",
        user="moany",
        password="password"
    )

    # db.get_transaction(db.get_connection())
    # db.get_transaction(db.get_connection())
    # db.get_transaction(db.get_connection())
    results = db.get_transaction(db.get_connection())
    print(f'count = {len(results)}')

    print("\n".join(results))
