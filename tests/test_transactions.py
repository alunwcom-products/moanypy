import db


def test_get_transactions():

    db.database_connection(
        database="moany",
        user="moany",
        password="password"
    )

    results = db.get_transactions(db.get_connection(),
                                  accounts=[
                                      '3ec51c2c-34bb-4b99-ad60-9a11f46a7335',
                                      '0d2d7abc-ab87-49e0-960a-1c38324aaf06']
                                  ,
                                  from_date='2020-12-11',
                                  to_date='2020-12-17',
                                  text='E',
                                  offset=0,
                                  limit=5)

    print(
        f'Metadata: total = {results.total}; offset = {results.offset}; limit = {results.limit}; '
        f'count = {len(results.transactions)}')
    for t in results.transactions:
        print(f'{t.trans_date} {t.net_amount:>9} [{t.account_id}]    "{t.description}"|"{t.comment}"')

    assert len(results) > 1
