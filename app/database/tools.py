import os
import os.path
import sqlite3


PATH_DATABASE_SCHEMA_MAIN = os.path.join(os.path.dirname(__file__), r"../../res/sql/schemas/main.sql")


def initialize_databases():
    global PATH_DATABASE_MAIN

    # Create the directory of the databases if it does not exists
    os.makedirs(PATH_DATABASE_MAIN, exist_ok=True)

    sqlite3.connect(PATH_DATABASE_MAIN).close()


def connexion(database="main"):
    global PATH_DATABASE_MAIN

    database = database.lower()
    if database == "main":
        return sqlite3.connect(PATH_DATABASE_MAIN)
    else:
        return None


def create_tables():
    global PATH_DATABASE_SCHEMA_MAIN

    # Retrieve the databases schemas
    with open(PATH_DATABASE_SCHEMA_MAIN) as f:
        statements_main = f.read()

    # Execute all the statements
    with connexion(database="main") as conn:
        cursor = conn.cursor()
        cursor.executescript(statements_main)


def get_all_tables():
    statement = """
        SELECT name
        FROM sqlite_master
        WHERE type='table';
    """

    with connexion("main") as conn:
        cursor = conn.cursor()
        cursor.execute(statement)
        all_tables = cursor.fetchall()


def clear_database():
    statement_main = """
        DELETE FROM User;
        DELETE FROM Guest;
        DELETE FROM UserHealth;
        DELETE FROM ConnexionToken;
        DELETE FROM SCB;
        DELETE FROM Rent;
        DELETE FROM User;
    """

    with connexion("main") as conn:
        cursor = conn.cursor()
        cursor.executescript(statement_main)


def execute_request(sql_request, database):
    """ Execute arbitrary SQL request into a specific database.
    This method is highly dangerous and thus must be protected to administrator only. Also, This is for debugging
    purposes. This method must not be included in any production-level code for security reasons.
    """
    with connexion(database) as conn:
        cursor = conn.cursor()
        cursor.execute(sql_request)
        return cursor.fetchall()


def row_factory(columns, row):
    """ Set the result as dictionaries instead of rows. """
    return dict([(column[0], row[i]) for i, column in enumerate(columns.description)])


def database_exists(database_name):
    return database_name.lower() in ("main", "issues", "poi", "picture")


if __name__ == "__main__":
    initialize_databases()
    create_tables()
