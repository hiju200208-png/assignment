import streamlit as st
import pandas as pd
import csv

st.title("💰 개인 지출 관리")

file_path = "chapter23/expenses.csv"


def load_expenses(file_path):
    expenses = []

    try:
        with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                try:
                    row["amount"] = int(row["amount"])
                except ValueError:
                    continue

                expenses.append(row)

    except FileNotFoundError:
        return []

    return expenses


def save_expenses(file_path, expenses):
    fieldnames = ["date", "category", "description", "amount"]

    with open(file_path, "w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(expenses)


# CSV에서 기존 데이터 불러오기
expenses = load_expenses(file_path)


st.subheader("지출 추가")

date = st.date_input("날짜")
category = st.text_input("카테고리")
description = st.text_input("내용")
amount = st.number_input(
    "금액",
    min_value=0,
    step=1000
)


if st.button("지출 추가"):

    if not category.strip() or not description.strip():
        st.error("카테고리와 내용을 입력해 주세요.")

    elif amount <= 0:
        st.error("금액은 0보다 큰 값으로 입력해 주세요.")

    else:
        expense = {
            "date": str(date),
            "category": category.strip(),
            "description": description.strip(),
            "amount": int(amount),
        }

        # 1. 리스트에 추가
        expenses.append(expense)

        # 2. CSV 저장
        save_expenses(file_path, expenses)

        # 3. 성공 메시지
        st.success("지출 내역을 추가했습니다.")

        # 4. 화면 다시 실행
        st.rerun()


st.subheader("지출 목록")

if expenses:
    df = pd.DataFrame(expenses)

    st.dataframe(df, use_container_width=True)

    total = sum(expense["amount"] for expense in expenses)

    st.metric(
        "전체 지출",
        f"{total:,}원"
    )

else:
    st.info("등록된 지출이 없습니다.")