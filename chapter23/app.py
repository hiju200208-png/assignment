import altair as alt
import pandas as pd
import streamlit as st

from expense_service import (
    add_expense,
    get_expenses,
    delete_expense,
    calculate_total,
    calculate_by_category,
)

# =========================================================
# 페이지 설정
# =========================================================
st.set_page_config(
    page_title="My Wallet",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded",
)




# =========================================================
# CSS
# =========================================================
st.markdown(
    """
<style>

/* ---------------------------------------------------------
   전체 화면
--------------------------------------------------------- */

.stApp {
    background: #F7F9FC;
}

header[data-testid="stHeader"] {
    background: #F7F9FC;
}

.block-container {
    max-width: 1180px;
    padding-top: 3.5rem !important;
    padding-bottom: 4rem !important;
}


/* ---------------------------------------------------------
   타이포그래피
--------------------------------------------------------- */

.page-title {
    font-size: 38px;
    font-weight: 800;
    color: #172033;
    letter-spacing: -1px;
    margin-bottom: 6px;
}

.page-subtitle {
    font-size: 15px;
    color: #7B879D;
    margin-bottom: 32px;
}

.section-title {
    font-size: 21px;
    font-weight: 750;
    color: #172033;
    margin-top: 38px;
    margin-bottom: 16px;
}


/* ---------------------------------------------------------
   사이드바
--------------------------------------------------------- */

section[data-testid="stSidebar"] {
    background: #FFFFFF !important;
    border-right: 1px solid #E8EDF5;
}

.sidebar-logo {
    font-size: 23px;
    font-weight: 800;
    color: #172033;
    margin-bottom: 3px;
}

.sidebar-caption {
    font-size: 13px;
    color: #8A95A8;
    margin-bottom: 26px;
}

/* 메뉴 라디오 */
section[data-testid="stSidebar"] div[role="radiogroup"] {
    gap: 5px;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label {
    background: transparent;
    padding: 9px 11px;
    border-radius: 10px;
}


/* ---------------------------------------------------------
   KPI 카드
--------------------------------------------------------- */

.stat-card {
    background: #FFFFFF;
    border: 1px solid #E5EBF5;
    border-radius: 16px;
    padding: 22px 24px;
    min-height: 118px;
    box-shadow: 0 5px 18px rgba(28, 62, 120, 0.045);
}

.stat-label {
    color: #8591A5;
    font-size: 13px;
    font-weight: 600;
    margin-bottom: 10px;
}

.stat-value {
    color: #1E5EFF;
    font-size: 29px;
    line-height: 1.1;
    font-weight: 800;
}


/* ---------------------------------------------------------
   흰색 패널
--------------------------------------------------------- */

.panel {
    background: #FFFFFF;
    border: 1px solid #E5EBF5;
    border-radius: 16px;
    padding: 22px;
    box-shadow: 0 5px 18px rgba(28, 62, 120, 0.04);
}


/* ---------------------------------------------------------
   Form
--------------------------------------------------------- */

div[data-testid="stForm"] {
    background: #FFFFFF !important;
    border: 1px solid #E5EBF5 !important;
    border-radius: 16px !important;
    padding: 26px !important;
    box-shadow: 0 5px 18px rgba(28, 62, 120, 0.04);
}


/* ---------------------------------------------------------
   입력 요소
--------------------------------------------------------- */

div[data-baseweb="input"] {
    background: #FFFFFF !important;
}

div[data-baseweb="select"] > div {
    background: #FFFFFF !important;
    border-color: #DDE5F0 !important;
    border-radius: 10px !important;
}

input {
    color: #172033 !important;
}

label {
    color: #536078 !important;
    font-weight: 600 !important;
}


/* ---------------------------------------------------------
   버튼
--------------------------------------------------------- */

.stButton > button,
.stFormSubmitButton > button {
    width: 100%;
    background: #2563EB !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 10px !important;
    min-height: 46px;
    font-weight: 700 !important;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    background: #1D4ED8 !important;
    color: #FFFFFF !important;
}


/* ---------------------------------------------------------
   Dataframe
--------------------------------------------------------- */

div[data-testid="stDataFrame"] {
    border: 1px solid #E5EBF5;
    border-radius: 14px;
    overflow: hidden;
    background: #FFFFFF;
}


/* ---------------------------------------------------------
   알림
--------------------------------------------------------- */

div[data-testid="stAlert"] {
    border-radius: 12px;
}

</style>
""",
    unsafe_allow_html=True
)


# =========================================================
# 데이터
# =========================================================
expenses = get_expenses()

if expenses:
    df = pd.DataFrame(expenses)

    df["amount"] = pd.to_numeric(
        df["amount"],
        errors="coerce"
    )

    df = df.dropna(
        subset=["amount"]
    )

    df["amount"] = df["amount"].astype(int)

else:
    df = pd.DataFrame(
        columns=[
            "id",
            "date",
            "category",
            "description",
            "amount"
        ]
    )

# =========================================================
# 사이드바
# =========================================================
with st.sidebar:

    st.markdown(
        '<div class="sidebar-logo">💳 My Wallet</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-caption">Simple Expense Manager</div>',
        unsafe_allow_html=True
    )

    menu = st.radio(
        "메뉴",
        [
            "대시보드",
            "지출 추가",
            "지출 내역"
        ],
        label_visibility="collapsed"
    )


# =========================================================
# 대시보드
# =========================================================
if menu == "대시보드":

    st.markdown(
        '<div class="page-title">대시보드</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        '나의 지출 현황을 한눈에 확인해보세요.'
        '</div>',
        unsafe_allow_html=True
    )


    if not df.empty:
        total = calculate_total(expenses)
        count = len(df)
        max_expense = int(df["amount"].max())

    else:
        total = 0
        count = 0
        max_expense = 0


    # -----------------------------------------------------
    # KPI
    # -----------------------------------------------------
    col1, col2, col3 = st.columns(3)


    with col1:
        st.markdown(
            f"""
<div class="stat-card">
    <div class="stat-label">총 지출</div>
    <div class="stat-value">{total:,}원</div>
</div>
""",
            unsafe_allow_html=True
        )


    with col2:
        st.markdown(
            f"""
<div class="stat-card">
    <div class="stat-label">지출 건수</div>
    <div class="stat-value">{count}건</div>
</div>
""",
            unsafe_allow_html=True
        )


    with col3:
        st.markdown(
            f"""
<div class="stat-card">
    <div class="stat-label">최대 지출</div>
    <div class="stat-value">{max_expense:,}원</div>
</div>
""",
            unsafe_allow_html=True
        )


    # -----------------------------------------------------
    # 카테고리 차트
    # -----------------------------------------------------
    st.markdown(
        '<div class="section-title">카테고리별 지출</div>',
        unsafe_allow_html=True
    )


    if not df.empty:

        category_df = (
            df.groupby(
                "category",
                as_index=False
            )["amount"]
            .sum()
            .sort_values(
                "amount",
                ascending=False
            )
        )


        base = alt.Chart(
            category_df
        ).encode(

            x=alt.X(
                "category:N",
                title=None,
                sort="-y",
                axis=alt.Axis(
                    labelAngle=0,
                    labelColor="#68758A",
                    labelFontSize=13,
                    ticks=False,
                    domain=False
                )
            ),

            y=alt.Y(
                "amount:Q",
                title=None,
                axis=alt.Axis(
                    labelColor="#8A95A8",
                    labelFontSize=11,
                    gridColor="#EEF2F7",
                    gridOpacity=1,
                    domain=False,
                    ticks=False,
                    format=",d"
                )
            )
        )


        bars = base.mark_bar(
            color="#4F7DF3",
            cornerRadiusTopLeft=7,
            cornerRadiusTopRight=7,
            size=80
        )


        labels = base.mark_text(
            dy=-12,
            color="#536078",
            fontSize=12,
            fontWeight=600
        ).encode(
            text=alt.Text(
                "amount:Q",
                format=","
            )
        )


        chart = (
            bars + labels
        ).properties(
            height=310
        ).configure_view(
            strokeWidth=0,
            fill="#FFFFFF"
        ).configure(
            background="#FFFFFF"
        )


        st.altair_chart(
            chart,
            use_container_width=True
        )


    else:
        st.info("등록된 지출이 없습니다.")


    # -----------------------------------------------------
    # 최근 지출
    # -----------------------------------------------------
    st.markdown(
        '<div class="section-title">최근 지출</div>',
        unsafe_allow_html=True
    )


    if not df.empty:

        recent_df = (
            df[
                [
                    "date",
                    "category",
                    "description",
                    "amount"
                ]
            ]
            .head(5)
            .copy()
        )

        recent_df.columns = [
            "날짜",
            "카테고리",
            "내용",
            "금액"
        ]

        st.dataframe(
            recent_df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "금액": st.column_config.NumberColumn(
                    "금액",
                    format="%d원"
                )
            }
        )

    else:
        st.info("최근 지출 내역이 없습니다.")


# =========================================================
# 지출 추가
# =========================================================
elif menu == "지출 추가":

    st.markdown(
        '<div class="page-title">지출 추가</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        '오늘 사용한 지출을 간단하게 기록해보세요.'
        '</div>',
        unsafe_allow_html=True
    )

    if st.session_state.get("expense_added"):
        st.success("✅ 지출이 추가되었습니다.")
        st.session_state["expense_added"] = False


    category_options = {
        "🍚 식비": "식비",
        "🚌 교통": "교통",
        "☕ 카페": "카페",
        "🛍️ 쇼핑": "쇼핑",
        "🏠 생활": "생활",
        "🎬 문화": "문화",
        "💊 의료": "의료",
        "📚 교육": "교육",
        "📦 기타": "기타"
    }


    with st.form("expense_form"):

        col1, col2 = st.columns(2)


        with col1:
            date = st.date_input(
                "날짜"
            )

            selected_category = st.selectbox(
                "카테고리",
                category_options.keys()
            )


        with col2:
            description = st.text_input(
                "내용",
                placeholder="예: 친구와 점심"
            )

            amount = st.number_input(
                "금액",
                min_value=0,
                step=1000
            )


        st.write("")

        submitted = st.form_submit_button(
            "지출 추가"
        )


    if submitted:

        category = category_options[
            selected_category
        ]


        if not description.strip():

            st.error(
                "내용을 입력해 주세요."
            )


        elif amount <= 0:

            st.error(
                "금액은 0보다 큰 값으로 입력해 주세요."
            )


        else:
            add_expense(
                str(date),
                category,
                description.strip(),
                int(amount)
            )

            st.session_state["expense_added"] = True

            st.rerun()


# =========================================================
# 지출 내역
# =========================================================
elif menu == "지출 내역":

    st.markdown(
        '<div class="page-title">지출 내역</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="page-subtitle">'
        '저장된 모든 지출 기록을 확인할 수 있습니다.'
        '</div>',
        unsafe_allow_html=True
    )


    if not df.empty:

        display_df = df[
            [
                "date",
                "category",
                "description",
                "amount"
            ]
        ].copy()

        display_df.columns = [
            "날짜",
            "카테고리",
            "내용",
            "금액"
        ]


        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True,
            column_config={

                "금액":
                    st.column_config.NumberColumn(
                        "금액",
                        format="%d원"
                    )
            }
        )

                # -------------------------------------------------
        # 지출 삭제
        # -------------------------------------------------
        st.markdown(
            '<div class="section-title">지출 삭제</div>',
            unsafe_allow_html=True
        )

        delete_options = {}

        for expense in expenses:
            label = (
                f"{expense['date']} | "
                f"{expense['category']} | "
                f"{expense['description']} | "
                f"{expense['amount']:,}원"
            )

            delete_options[label] = expense["id"]

        selected_delete = st.selectbox(
            "삭제할 지출 선택",
            delete_options.keys()
        )

        if st.button("선택한 지출 삭제"):

            expense_id = delete_options[selected_delete]

            delete_expense(expense_id)

            st.session_state["expense_deleted"] = True

            st.rerun()




        total = int(
            df["amount"].sum()
        )


        st.write("")


        st.markdown(
            f"""
<div class="stat-card" style="max-width:320px;">
    <div class="stat-label">전체 지출</div>
    <div class="stat-value">{total:,}원</div>
</div>
""",
            unsafe_allow_html=True
        )


    else:
        st.info(
            "등록된 지출이 없습니다."
        )