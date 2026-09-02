from expense_service import (
    add_expense,
    get_expenses,
    delete_expense,
    calculate_total,
    calculate_by_category,
)


# =========================================================
# 지출 추가 입력
# =========================================================
def input_expense():
    date = input("날짜(YYYY-MM-DD): ").strip()
    category = input("카테고리: ").strip()
    description = input("내용: ").strip()

    if not date or not category or not description:
        print("날짜, 카테고리, 내용은 비워 둘 수 없습니다.")
        return

    try:
        amount = int(input("금액: "))

    except ValueError:
        print("금액은 정수로 입력해 주세요.")
        return

    if amount <= 0:
        print("금액은 0보다 큰 값으로 입력해 주세요.")
        return

    # 공통 함수 사용 → PostgreSQL 저장
    add_expense(
        date,
        category,
        description,
        amount
    )

    print("지출 내역을 추가했습니다.")


# =========================================================
# 지출 목록 출력
# =========================================================
def show_expenses():
    # 공통 함수 사용 → PostgreSQL 조회
    expenses = get_expenses()

    if not expenses:
        print("등록된 지출이 없습니다.")
        return

    print("\n=== 지출 내역 ===")

    for expense in expenses:
        print(
            f"{expense['id']}. "
            f"{expense['date']} | "
            f"{expense['category']} | "
            f"{expense['description']} | "
            f"{expense['amount']:,}원"
        )


# =========================================================
# 지출 요약
# =========================================================
def show_summary():
    # PostgreSQL에서 현재 데이터 가져오기
    expenses = get_expenses()

    total = calculate_total(expenses)
    category_totals = calculate_by_category(expenses)

    print("\n=== 지출 요약 ===")

    print(f"전체 지출: {total:,}원")

    print("\n카테고리별 지출")

    if not category_totals:
        print("등록된 지출이 없습니다.")
        return

    for category, amount in category_totals.items():
        print(f"{category}: {amount:,}원")


# =========================================================
# 지출 삭제
# =========================================================
def remove_expense():
    expenses = get_expenses()

    if not expenses:
        print("삭제할 지출이 없습니다.")
        return

    print("\n=== 지출 내역 ===")

    for expense in expenses:
        print(
            f"{expense['id']}. "
            f"{expense['date']} | "
            f"{expense['category']} | "
            f"{expense['description']} | "
            f"{expense['amount']:,}원"
        )

    try:
        expense_id = int(
            input("\n삭제할 지출 ID: ")
        )

    except ValueError:
        print("ID는 숫자로 입력해 주세요.")
        return

    # 실제 존재하는 ID인지 확인
    expense_ids = [
        expense["id"]
        for expense in expenses
    ]

    if expense_id not in expense_ids:
        print("해당 ID의 지출이 없습니다.")
        return

    # 공통 함수 사용 → PostgreSQL 삭제
    delete_expense(expense_id)

    print("지출 내역을 삭제했습니다.")


# =========================================================
# 메인 메뉴
# =========================================================
while True:

    print("\n======================")
    print("   개인 지출 관리")
    print("======================")

    print("1. 지출 추가")
    print("2. 지출 목록")
    print("3. 지출 요약")
    print("4. 지출 삭제")
    print("0. 종료")

    choice = input("메뉴 선택: ").strip()

    if choice == "1":
        input_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        show_summary()

    elif choice == "4":
        remove_expense()

    elif choice == "0":
        print("프로그램을 종료합니다.")
        break

    else:
        print("메뉴 번호를 다시 선택해 주세요.")