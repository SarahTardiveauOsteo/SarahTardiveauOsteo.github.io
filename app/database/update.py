from .tools import connexion


def cancel_reservation(id_reservation):
    statement = """
        UPDATE Reservation
        SET is_canceled=1
        WHERE id=?;
    """

    with connexion() as conn:
        cursor = conn.cursor()
        cursor.execute(statement, (id_reservation,))


if __name__ == "__main__":
    pass
