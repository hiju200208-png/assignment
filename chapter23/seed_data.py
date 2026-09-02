import random
from datetime import date, timedelta

from expense_service import add_expense


# =========================================================
# 설정
# =========================================================

START_DATE = date(2025, 9, 1)
END_DATE = date(2026, 8, 31)


expense_examples = {
    "식비": [
        ("점심", 8000, 15000),
        ("저녁", 10000, 25000),
        ("간식", 2000, 8000),
    ],

    "교통": [
        ("버스", 1500, 3000),
        ("지하철", 1500, 3000),
        ("택시", 7000, 25000),
    ],

    "카페": [
        ("커피", 3000, 7000),
        ("디저트", 4000, 10000),
    ],

    "쇼핑": [
        ("의류", 20000, 100000),
        ("생활용품", 5000, 40000),
    ],

    "생활": [
        ("생필품", 5000, 30000),
        ("편의점", 2000, 15000),
    ],

    "문화": [
        ("영화", 12000, 20000),
        ("전시", 10000, 30000),
    ],

    "의료": [
        ("병원", 5000, 50000),
        ("약국", 3000, 20000),
    ],

    "교육": [
        ("책", 10000, 40000),
        ("강의", 20000, 100000),
    ],
}


# =========================================================
# 1년치 데이터 생성
# =========================================================

current_date = START_DATE
count = 0


while current_date <= END_DATE:

    # 하루에 1~3개의 지출 생성
    daily_count = random.randint(1, 3)

    for _ in range(daily_count):

        category = random.choice(
            list(expense_examples.keys())
        )

        description, min_amount, max_amount = random.choice(
            expense_examples[category]
        )

        # 500원 단위 금액 생성
        amount = random.randrange(
            min_amount,
            max_amount + 1,
            500
        )

        add_expense(
            str(current_date),
            category,
            description,
            amount
        )

        count += 1

    current_date += timedelta(days=1)


print("============================")
print("1년치 데이터 생성 완료!")
print(f"기간: {START_DATE} ~ {END_DATE}")
print(f"총 {count}건이 추가되었습니다.")
print("============================")