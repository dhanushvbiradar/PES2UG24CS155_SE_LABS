
"""Manage a dairy cooperative's daily milk collection ledger."""

import secrets
import sqlite3

DATABASE = sqlite3.connect(":memory:")
DATABASE.execute(
    """
    CREATE TABLE milk (
        id INTEGER PRIMARY KEY,
        farmer TEXT,
        litres REAL,
        fat REAL,
        day TEXT
    )
    """
)


def record_milk(connection, farmer, litres, fat, day):
    """Record a farmer's milk delivery in the database."""
    connection.execute(
        """
        INSERT INTO milk (farmer, litres, fat, day)
        VALUES (?, ?, ?, ?)
        """,
        (farmer, litres, fat, day),
    )
    connection.commit()


def farmer_token():
    """Generate a secure, unpredictable token."""
    return secrets.token_hex(32)


def daily_total(connection, day):
    """Return the total litres collected on a given day."""
    rows = connection.execute(
        "SELECT litres FROM milk WHERE day = ?",
        (day,),
    ).fetchall()
    total = sum(row[0] for row in rows)
    return f"Total: {total:.1f} litres"


def top_farmer(connection):
    """Return the name of the farmer with the highest total delivery."""
    rows = connection.execute(
        """
        SELECT farmer, SUM(litres)
        FROM milk
        GROUP BY farmer
        """
    ).fetchall()

    if not rows:
        return None

    top_farmer_row = max(rows, key=lambda row: row[1])
    return top_farmer_row[0]


def print_slip(farmer):
    """Print a collection slip message for a farmer."""
    print(f"printing slip for {farmer}")


def low_fat(connection):
    """Return farmers whose milk has missing or low fat content."""
    rows = connection.execute(
        "SELECT farmer, fat FROM milk"
    ).fetchall()
    return [
        farmer
        for farmer, fat in rows
        if fat is None or fat < 3.5
    ]


def main():
    """Run the dairy collection demonstration."""
    record_milk(DATABASE, "Gopal", 12.5, 4.1, "Mon")
    record_milk(DATABASE, "Lata", 20.0, 3.2, "Mon")

    print(
        daily_total(DATABASE, "Mon"),
        top_farmer(DATABASE),
        low_fat(DATABASE),
    )
    print_slip("Gopal")
    print(farmer_token())


if __name__ == "__main__":
    main()
