from db import get_connection


# ==========================================
# 지출 추가
# ==========================================
def add_expense(date, category, description, amount):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO expenses
            (date, category, description, amount)
        VALUES
            (%s, %s, %s, %s)
        """,
        (date, category, description, amount)
    )

    conn.commit()

    cursor.close()
    conn.close()


# ==========================================
# 전체 지출 조회
# ==========================================
def get_expenses():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            id,
            date,
            category,
            description,
            amount
        FROM expenses
        ORDER BY date DESC, id DESC
        """
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    expenses = []

    for row in rows:
        expense = {
            "id": row[0],
            "date": str(row[1]),
            "category": row[2],
            "description": row[3],
            "amount": row[4]
        }

        expenses.append(expense)

    return expenses


# ==========================================
# 지출 삭제
# ==========================================
def delete_expense(expense_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM expenses
        WHERE id = %s
        """,
        (expense_id,)
    )

    conn.commit()

    cursor.close()
    conn.close()


# ==========================================
# 전체 지출 계산
# ==========================================
def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


# ==========================================
# 카테고리별 지출 계산
# ==========================================
def calculate_by_category(expenses):
    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

    return category_totals