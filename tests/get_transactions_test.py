import db

if __name__ == "__main__":
    db.database_connection(
        database="moany",
        user="moany",
        password="password"
    )

    results = db.get_transactions(db.get_connection(), 200, 5)

    print(
        f'Metadata: total = {results.total}; offset = {results.offset}; limit = {results.limit}; count = {len(results.results)}')
    for t in results.results:
        print(f'{t.trans_date} {t.net_amount:>9} [{t.account_id}]    {t.description}')
