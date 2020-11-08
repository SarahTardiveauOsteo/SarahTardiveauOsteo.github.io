from .tools import connexion


def user(id_user):
    statement = """
        DELETE
        FROM User
        WHERE id=?;
    """

    with connexion() as conn:
        cursor = conn.cursor()
        cursor.execute(statement, (id_user,))


if __name__ == "__main__":
    pass
