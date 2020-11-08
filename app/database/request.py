from .tools import connexion


def is_existing_reservation(id_reservation):
    statement = """
        SELECT *
        FROM Reservation
        WHERE id=?;
    """

    with connexion() as conn:
        cursor = conn.cursor()
        cursor.execute(statement, (id_reservation,))
        return bool(cursor.fetchone())


def list_all_reservations_by_user(id_user):
    statement = """
        SELECT *
        FROM Reservation
        WHERE id_user=?;
    """

    with connexion() as conn:
        cursor = conn.cursor()
        cursor.execute(statement, (id_user,))
        return cursor.fetchall()


if __name__ == "__main__":
    pass
