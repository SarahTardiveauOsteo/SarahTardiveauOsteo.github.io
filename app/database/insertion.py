from .tools import connexion


def user(first_name, last_name, birthday, email, phone_number):
    statement = """
        INSERT INTO User (first_name, last_name, birthday, email, phone_number)
        VALUES (?, ?, ?, ?, ?);
    """

    with connexion() as conn:
        cursor = conn.cursor()
        cursor.execute(statement, (first_name, last_name, birthday, email, phone_number))


def reservation(id_user, reservation_date_start, reservation_date_end):
    statement = """
        INSERT INTO Reservation (id_user, reservation_date_start, reservation_date_end)
        VALUES (?, ?, ?);
    """

    with connexion() as conn:
        cursor = conn.cursor()
        cursor.execute(statement, (id_user, reservation_date_start, reservation_date_end))


if __name__ == "__main__":
    pass
