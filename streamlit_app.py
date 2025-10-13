import streamlit as st
import random

# 커스텀 버튼 폰트 크기 줄이기
st.markdown(
    """
    <style>
    div.stButton > button {
        font-size: 0.7rem !important;
        padding: 0.2em 0.5em !important;
        white-space: nowrap !important;
        min-width: 70px !important;
        max-width: 100px !important;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🔢 10진수를 2진수로 변환하는 앱")

# 1. 0~1023 사이의 랜덤한 10진수 생성 (세션에 저장)
if 'decimal' not in st.session_state:
    st.session_state.decimal = random.randint(0, 1023)
decimal = st.session_state.decimal

st.write(f"랜덤 10진수: **{decimal}**")

# 2. 사용자에게 2진수로 몇 비트가 필요한지 입력 받기
min_bits = decimal.bit_length() if decimal > 0 else 1
user_bits = st.number_input(
    "이 숫자를 2진수로 표현하려면 몇 비트가 필요할까요?", 
    min_value=1, max_value=10, step=1
)

if st.button("정답 확인"):
    if user_bits == min_bits:
        st.success(f"정답입니다! {decimal}을(를) 2진수로 표현하려면 {min_bits}비트가 필요합니다.")
        st.session_state.correct = True
    else:
        st.error(f"틀렸습니다. 다시 시도해보세요!")
        st.session_state.correct = False

# 3. 정답을 맞췄을 때만 버튼 생성
if st.session_state.get('correct', False):

    st.write("아래 버튼을 눌러 2진수로 만들어보세요!")
    if 'bits' not in st.session_state or len(st.session_state.bits) != user_bits:
        st.session_state.bits = [False] * user_bits

    cols = st.columns(user_bits)
    weights = [2**i for i in reversed(range(user_bits))]  # MSB~LSB

    # 1. 버튼 행
    for i, col in enumerate(cols):
        with col:
            if st.button(f"{user_bits-i-1}번 비트", key=f"bit_btn_{i}"):
                st.session_state.bits[i] = not st.session_state.bits[i]

    # 2. 가중치 행
    for i, col in enumerate(cols):
        with col:
            st.markdown(f"<div style='text-align:center; color:gray; margin-top:4px'>{weights[i]}</div>", unsafe_allow_html=True)

    # 3. 선택값 행
    for i, col in enumerate(cols):
        with col:
            val = "1" if st.session_state.bits[i] else "0"
            color = "#4CAF50" if st.session_state.bits[i] else "#ddd"
            st.markdown(f"<div style='text-align:center; background:{color}; border-radius:5px; padding:4px 0; margin-top:4px'>{val}</div>", unsafe_allow_html=True)

    # 4. 합계 행 (각 열별로 합산값 표시, 선택된 비트만 값, 아니면 0)
    for i, col in enumerate(cols):
        with col:
            show_val = weights[i] if st.session_state.bits[i] else 0
            st.markdown(f"<div style='text-align:center; color:#333; margin-top:4px; font-size:0.9em'>{show_val}</div>", unsafe_allow_html=True)

    # 5. 전체 합계
    selected_value = sum(w if b else 0 for w, b in zip(weights, st.session_state.bits))
    st.write("")  # 간격
    st.write(f"선택한 비트의 합: **{selected_value}**")

    # 5. 최종적으로 정답 확인
    if selected_value == decimal:
        st.success(f"정답! {decimal}의 2진수는 {bin(decimal)[2:].zfill(user_bits)} 입니다.")
    else:
        st.info("아직 정답이 아닙니다. 버튼을 조정해보세요.")

    if st.button("새 문제"):
        st.session_state.clear()
        st.experimental_rerun()
