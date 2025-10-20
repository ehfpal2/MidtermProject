import streamlit as st
import random


st.title("💡 2진수를 10진수로 변환하는 앱")

# 1. 1~10비트 길이의 랜덤 2진수 생성 (1이 반드시 포함되도록)
if 'bit_len' not in st.session_state:
    st.session_state.bit_len = random.randint(1, 10)
if 'binary' not in st.session_state:
    while True:
        bits = [random.choice([0, 1]) for _ in range(st.session_state.bit_len)]
        if bits.count(1) >= 2:  # 1이 두 개 이상 포함되어 있으면 OK
            st.session_state.binary = bits
            break

bit_len = st.session_state.bit_len
binary = st.session_state.binary

# 2진수 표시 (MSB~LSB)
bin_str = ''.join(str(b) for b in binary)
st.write(f"랜덤 2진수: <span style='font-size:1.5em; letter-spacing:0.2em'><b>{bin_str}</b></span>", unsafe_allow_html=True)


# 각 비트별로 입력 칸 생성 (MSB~LSB)
st.write("각 비트 아래 칸에 1로 표현된 자리의 가중치를 입력하세요. (해당 비트가 1일 때는 숫자, 0일 때는 0 또는 빈칸)")
cols = st.columns(bit_len)
if 'user_weights' not in st.session_state or len(st.session_state.user_weights) != bit_len:
    st.session_state.user_weights = [''] * bit_len

for i, col in enumerate(cols):
    with col:
        # 비트값 가운데 정렬
        st.markdown(f"<div style='text-align:center; font-weight:bold'>{binary[i]}</div>", unsafe_allow_html=True)
        # 입력 칸 가운데 정렬 및 라벨 제거
        st.markdown("""
        <style>
        .centered-input input {
            text-align: center !important;
        }
        </style>
        """, unsafe_allow_html=True)
        st.session_state.user_weights[i] = st.text_input(
            label=" ",  # 라벨 없이
            value=st.session_state.user_weights[i],
            key=f"weight_input_{i}",
            placeholder=""
        )
        # 입력 칸에 클래스 적용 (streamlit 기본 input에는 직접 class 적용이 어려워 스타일로 전체 적용)

# 정답 가중치 계산
def get_weights(bits):
    return [2**i for i, b in enumerate(reversed(bits)) if b == 1]

answer_weights = get_weights(binary)


if st.button("정답 확인"):
    try:
        # 입력된 값 중 비어있지 않고, 해당 비트가 1인 칸만 추출
        user_weights = [int(st.session_state.user_weights[i]) for i in range(bit_len) if binary[i] == 1 and st.session_state.user_weights[i].strip()]
        if sorted(user_weights) == sorted(answer_weights):
            st.success("정답입니다! 이제 각 가중치의 합을 계산해보세요.")
            st.session_state.show_calc = True
        else:
            st.error(f"틀렸습니다. 정답: {answer_weights}")
            st.session_state.show_calc = False
    except Exception:
        st.error("입력 형식이 올바르지 않습니다. 숫자만 입력하세요.")

# 2. 정답이면 계산기 표시
if st.session_state.get('show_calc', False):
    st.markdown("<span style='font-size:1.3em'>각 가중치를 더해 10진수 값을 입력하세요!</span>", unsafe_allow_html=True)
    user_decimal = st.number_input("10진수 값 입력", min_value=0, step=1)
    decimal_value = sum(answer_weights)
    if st.button("최종 정답 확인"):
        if user_decimal == decimal_value:
            st.success(f"정답! 2진수 {bin_str}의 10진수 값은 {decimal_value}입니다.")
        else:
            st.error(f"틀렸습니다. 정답은 {decimal_value}입니다.")

# 새 문제 버튼
if st.button("새 문제"):
    for k in ['bit_len', 'binary', 'show_calc']:
        if k in st.session_state:
            del st.session_state[k]
    st.experimental_rerun()
