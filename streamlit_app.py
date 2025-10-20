# ...existing code...
import streamlit as st

st.set_page_config(page_title="진법 변환기", page_icon="🔢")

# 버튼을 한 줄 전체 너비로 만들기 위한 간단한 스타일
st.markdown(
    """
    <style>
    div.stButton > button {
        width: 100% !important;
        font-size: 1rem !important;
        padding: 0.6em 0.8em !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("진법 변환기")
st.write("원하는 변환 페이지를 왼쪽에서 선택하세요.")

# 1줄씩 버튼을 배치 (각 버튼은 별도 컨테이너에 있어 한 줄 차지)
with st.container():
    if st.button("10진수 → 2진수 (change1)"):
        # 전체 URL이 아니라 페이지 이름(또는 간단한 값)만 설정
        st.experimental_set_query_params(page="/workspaces/MidtermProject/pages/change1.py")
        st.experimental_rerun()


with st.container():
    if st.button("2진수 → 10진수 (change2)"):
        st.experimental_set_query_params(page="/workspaces/MidtermProject/pages/change2.py")
        st.experimental_rerun()
