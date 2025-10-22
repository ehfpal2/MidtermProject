import streamlit as st
import random

# 🔹 버튼 스타일 (폰트 크기 줄이기)
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

# ===============================
# 문제 고유 ID 생성 (새 문제 시 키를 분리하기 위함)
# ===============================
if 'problem_id' not in st.session_state:
    st.session_state.problem_id = 0
pid = st.session_state.problem_id

# 1. 랜덤 10진수 생성
if f'decimal_{pid}' not in st.session_state:
    st.session_state[f'decimal_{pid}'] = random.randint(0, 1023)
decimal = st.session_state[f'decimal_{pid}']

st.write(f"랜덤 10진수: **{decimal}**")

# 2. 사용자에게 필요한 비트 수 입력
min_bits = decimal.bit_length() if decimal > 0 else 1
user_bits = st.number_input(
    "이 숫자를 2진수로 표현하려면 몇 비트가 필요할까요?",
    min_value=1, max_value=10, step=1,
    key=f"bit_input_{pid}"
)

if st.button("정답 확인", key=f"check_btn_{pid}"):
    if user_bits == min_bits:
        st.success(f"정답입니다! {decimal}을(를) 2진수로 표현하려면 {min_bits}비트가 필요합니다.")
        st.session_state[f'correct_{pid}'] = True
    else:
        st.error("틀렸습니다. 다시 시도해보세요!")
        st.session_state[f'correct_{pid}'] = False

# 3. 정답 맞췄을 때만 2진수 구성 인터페이스 표시
if st.session_state.get(f'correct_{pid}', False):

    st.write("아래 버튼을 눌러 2진수로 만들어보세요!")

    # 비트 배열 초기화
    if f'bits_{pid}' not in st.session_state or len(st.session_state[f'bits_{pid}']) != user_bits:
        st.session_state[f'bits_{pid}'] = [False] * user_bits

    cols = st.columns(user_bits)
    weights = [2**i for i in reversed(range(user_bits))]  # MSB~LSB

    # 1️⃣ 비트 버튼 행
    for i, col in enumerate(cols):
        with col:
            if st.button(f"{user_bits-i-1}번 비트", key=f"bit_btn_{pid}_{i}"):
                st.session_state[f'bits_{pid}'][i] = not st.session_state[f'bits_{pid}'][i]

    # 2️⃣ 가중치 행
    for i, col in enumerate(cols):
        with col:
            st.markdown(
                f"<div style='text-align:center; color:gray; margin-top:4px'>{weights[i]}</div>",
                unsafe_allow_html=True
            )

    # 3️⃣ 선택된 비트 행
    for i, col in enumerate(cols):
        with col:
            val = "1" if st.session_state[f'bits_{pid}'][i] else "0"
            color = "#4CAF50" if st.session_state[f'bits_{pid}'][i] else "#ddd"
            st.markdown(
                f"<div style='text-align:center; background:{color}; border-radius:5px; padding:4px 0; margin-top:4px'>{val}</div>",
                unsafe_allow_html=True
            )

    # 4️⃣ 각 비트의 실제 값
    for i, col in enumerate(cols):
        with col:
            show_val = weights[i] if st.session_state[f'bits_{pid}'][i] else 0
            st.markdown(
                f"<div style='text-align:center; color:#333; margin-top:4px; font-size:0.9em'>{show_val}</div>",
                unsafe_allow_html=True
            )

    # 5️⃣ 전체 합계 계산
    selected_value = sum(w if b else 0 for w, b in zip(weights, st.session_state[f'bits_{pid}']))
    st.write("")
    st.write(f"선택한 비트의 합: **{selected_value}**")

    # 정답 여부
    if selected_value == decimal:
        st.success(f"정답! {decimal}의 2진수는 {bin(decimal)[2:].zfill(user_bits)} 입니다.")
    else:
        st.info("아직 정답이 아닙니다. 버튼을 조정해보세요.")

    # 🔄 새 문제 버튼
    if st.button("새 문제", key=f"new_problem_btn_{pid}"):
        # 문제 ID 증가 → 모든 key 분리
        st.session_state.problem_id += 1
        st.rerun()
