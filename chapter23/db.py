import psycopg2


def get_connection():
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        dbname="expense_db",
        user="postgres",
        password="alice200208"
    )

    return connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id SERIAL PRIMARY KEY,
            date DATE NOT NULL,
            category VARCHAR(50) NOT NULL,
            description VARCHAR(200) NOT NULL,
            amount INTEGER NOT NULL CHECK (amount > 0)
        );
    """)

    conn.commit()

    cursor.close()
    conn.close()

    print("expenses 테이블 생성 완료!")


if __name__ == "__main__":
    create_table()

if __name__ == "__main__":
    conn = get_connection()

    print("PostgreSQL 연결 성공!")

    conn.close()