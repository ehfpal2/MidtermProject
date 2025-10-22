import streamlit as st

# 페이지 설정
st.set_page_config(page_title="진법 변환기", page_icon="🔢", layout="centered")

# 스타일 지정
st.markdown(
    """
    <style>
    /* 전체 페이지 중앙 정렬 */
    .main {
        text-align: left !important;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    /* 제목 */
    h1 {
        text-align: left;
        color: #1565C0;
        font-size: 2.5em;
        margin-bottom: 0.3em;
    }

    /* 설명 문구 */
    .desc {
        text-align: left;
        font-size: 1.1rem;
        color: #333;
        margin-bottom: 2em;
    }

    /* 버튼 공통 스타일 */
    div.stButton > button {
        display: block;
        width: 300px !important;               /* 버튼 폭 고정 (중앙정렬 효과) */
        margin: 1em auto !important;           /* 가운데 + 버튼 간격 */
        font-size: 1.1rem !important;
        padding: 0.8em 1em !important;
        border: 2px solid #1E88E5 !important;  /* 파란색 테두리 */
        border-radius: 12px !important;        /* 둥근 모서리 */
        color: #1E88E5 !important;
        background-color: #F0F8FF !important;  /* 연한 파란 배경 */
        font-weight: 600 !important;
        transition: all 0.25s ease-in-out;
    }

    /* 버튼 호버 */
    div.stButton > button:hover {
        background-color: #1E88E5 !important;
        color: white !important;
        transform: scale(1.03);
    }

    /* 버튼 사이 제목 */
    .mid-title {
        font-size: 1.2rem;
        color: #0D47A1;
        font-weight: bold;
        text-align: left;
        margin: 1.5em 0 0.5em 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------------
# 본문 구성
# ----------------------------------
st.title("진법 변환기")
st.markdown("<p class='desc'>변환하고 싶은 방향을 선택하세요.</p>", unsafe_allow_html=True)

# 버튼 1 (가운데)
if st.button("🔹 10진수 → 2진수 (change1)"):
    st.switch_page("pages/change1.py")

# 중간 제목 (가운데)
st.markdown("<p class='mid-title'>⬇️ 반대로 변환하고 싶다면 ⬇️</p>", unsafe_allow_html=True)

# 버튼 2 (가운데)
if st.button("🔹 2진수 → 10진수 (change2)"):
    st.switch_page("pages/change2.py")

