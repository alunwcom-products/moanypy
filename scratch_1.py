import db
import decimal


if __name__ == "__main__":

    db.database_connection(
        database="moany",
        user="moany",
        password="password"
    )

    results = db.get_transactions(db.get_connection(),
                                  accounts=[
                                      '3ec51c2c-34bb-4b99-ad60-9a11f46a7335'
                                  ],
                                  # categories=[
                                  #     '88949c94-d5dd-4a4b-81af-10800c3a0b96',
                                  #     '68005144-e810-48b3-914b-5d371b7856c1'
                                  # ],
                                  from_date='2020-01-01',
                                  to_date='2020-12-31',
                                  text='',
                                  offset=0,
                                  limit=50)

    print(
        f'Metadata: total = {results.total}; offset = {results.offset}; limit = {results.limit}; '
        f'count = {len(results.transactions)}')

    # for t in results.transactions:
    #     print(f'{t.trans_date} {t.net_amount:>9} [{t.account_id}]    "{t.description}"|"{t.comment}"')

    # balance = 0
    # decimal.getcontext().prec = 2
    # balance = decimal.Decimal('-5.80') + decimal.Decimal('3887.09')
    # balance = decimal.Decimal('-37.47') + decimal.Decimal('3966.86')
    balance = decimal.Decimal('3966.86')
    amount = 0
    for t in results.transactions:
        print(f'{t.trans_date} {t.net_amount:>9} {balance:>9} [{t.account_balance:>9}] [{t.account_id}]    "{t.description}"|"{t.comment}"')
        balance = balance + t.net_amount


