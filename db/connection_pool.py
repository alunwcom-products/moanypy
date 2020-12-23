import mariadb

pool = None


def database_connection(database, user, password, host="localhost", port=3306, autocommit=False, poolsize=10):
    try:
        global pool
        pool = mariadb.ConnectionPool(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port,
            autocommit=autocommit,
            pool_name="moanypy",
            pool_size=poolsize
        )

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")


def get_connection():
    try:
        global pool
        print(f'pool = {pool}')
        return pool.get_connection()

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")
