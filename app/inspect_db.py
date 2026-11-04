from pprint import pprint

from app.db import get_connection


def main():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT TABLE_NAME
                FROM INFORMATION_SCHEMA.TABLES
                WHERE TABLE_SCHEMA = DATABASE()
                ORDER BY TABLE_NAME
                """
            )
            tables = [row[0] for row in cursor.fetchall()]

            print("Tables:")
            for table in tables:
                print(f"- {table}")

            if not tables:
                print("No tables found in the configured database.")
                return

            table = tables[0]
            quoted_table = "`" + table.replace("`", "``") + "`"

            cursor.execute(f"SHOW COLUMNS FROM {quoted_table}")
            columns = [row[0] for row in cursor.fetchall()]
            print(f"\nColumns in {table}:")
            pprint(columns)

            cursor.execute(f"SELECT * FROM {quoted_table} LIMIT 3")
            print(f"\nFirst 3 rows in {table}:")
            pprint(cursor.fetchall())
    finally:
        connection.close()


if __name__ == "__main__":
    main()
