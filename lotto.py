import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="로또 번호 생성기", page_icon="🎱")


# 로또 공 HTML 생성 함수 (줄바꿈 없이 한 줄로 작성)
def get_ball_html(number):
    if number <= 10:
        color, text_color = "#fbc400", "black"  # 노란색 (1~10)
    elif number <= 20:
        color, text_color = "#69c5f0", "white"  # 파란색 (11~20)
    elif number <= 30:
        color, text_color = "#ff4040", "white"  # 빨간색 (21~30)
    elif number <= 40:
        color, text_color = "#aaaaaa", "white"  # 회색 (31~40)
    else:
        color, text_color = "#b0d840", "black"  # 녹색 (41~45)

    # HTML 태그 내부에 줄바꿈이 없어야 Streamlit에서 문자로 깨지지 않고 동그란 공으로 정상 렌더링됩니다.
    return f'<div style="display:inline-block; width:45px; height:45px; line-height:45px; border-radius:50%; background-color:{color}; color:{text_color}; font-weight:bold; font-size:18px; text-align:center; margin:4px; box-shadow:1px 1px 3px rgba(0,0,0,0.2);">{number}</div>'


# 세션 상태 초기화 (생성된 로또 번호 세트 저장용)
if "lotto_history" not in st.session_state:
    st.session_state.lotto_history = []

st.title("🎱 로또 번호 생성기")

# [로또번호 생성] 버튼 클릭 이벤트
if st.button("로또번호 생성"):
    # 1~45 사이 중복 없는 6개 번호 추출 및 정렬
    new_numbers = sorted(random.sample(range(1, 46), 6))

    # 최신 생성 번호를 맨 앞에 추가
    st.session_state.lotto_history.insert(0, new_numbers)

    # 최대 5개 세트까지만 유지
    if len(st.session_state.lotto_history) > 5:
        st.session_state.lotto_history = st.session_state.lotto_history[:5]

# 저장된 로또 번호 세트 화면 출력
if st.session_state.lotto_history:
    st.write("---")
    for idx, numbers in enumerate(st.session_state.lotto_history, 1):
        # 6개 공 HTML을 하나로 연결
        balls_html = "".join([get_ball_html(num) for num in numbers])

        # 공 6개가 한 줄에 쫙 나란히 나오도록 출력
        st.markdown(
            f'<div style="display:flex; align-items:center; margin-bottom:10px;"><b style="margin-right:15px; font-size:16px;">{idx}번째 세트:</b> {balls_html}</div>',
            unsafe_allow_html=True,
        )

# 초기화 버튼
if st.session_state.lotto_history:
    if st.button("초기화"):
        st.session_state.lotto_history = []
        st.rerun()