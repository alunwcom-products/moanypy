import db


def test_get_accounts():

    db.database_connection(
        database="moany",
        user="moany",
        password="password"
    )
    results = db.get_accounts(db.get_connection())

    # print(results)

    assert len(results) == 7
