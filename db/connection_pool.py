import mysql.connector

# pool = None
POOL_NAME = 'default'


def database_connection(database, user, password, host="localhost", port=3306, autocommit=False, poolsize=10):
    try:
        dbconfig = {
            "database": "moany",
            "user": "moany",
            "password": "password"
        }
        connection = mysql.connector.connect(
            pool_name=POOL_NAME,
            pool_size=poolsize,
            database=database,
            user=user,
            password=password,
            host=host,
            port=port,
            autocommit=autocommit
        )

        # global pool
        # if not pool:
        #     pool = mariadb.ConnectionPool(
        #         database=database,
        #         user=user,
        #         password=password,
        #         host=host,
        #         port=port,
        #         autocommit=autocommit,
        #         pool_name="moanypy",
        #         pool_size=poolsize
        #     )

    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")


def get_connection():
    try:
        # global pool
        # print(f'pool = {pool}')
        # return pool.get_connection()

        return mysql.connector.connect(pool_name=POOL_NAME)

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")
