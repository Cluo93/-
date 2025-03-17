import streamlit as st
import random
import time

# 화면 설정
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 10  # 비행기와 총알 크기

# 색상 정의 (Streamlit에서는 직접 사용되지 않음)
GREEN = "green"  # 비행기 색상
RED = "red"  # 총알 색상

# 게임 상태 초기화
if "flight_pos" not in st.session_state:
    st.session_state.flight_pos = [WIDTH // 2, HEIGHT - 50]  # 비행기 위치 (중앙)
    st.session_state.bullets = []  # 총알 리스트
    st.session_state.score = 0  # 점수
    st.session_state.frame_count = 0  # 총알 추가 타이머
    for _ in range(3):  # 시작할 때 3개의 총알 생성
        bullet_pos = [random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)]
        bullet_speed = [random.choice([-3, 3]), random.choice([-3, 3])]
        st.session_state.bullets.append({"pos": bullet_pos, "speed": bullet_speed})

# 게임 속도 설정
speed = 0.03  # 초당 업데이트 속도

# 타이틀
st.title("✈️ 비행기 피하기 게임 (Streamlit)")

# 방향키 조작 버튼
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⬅️ 왼쪽"):
        st.session_state.flight_pos[0] -= CELL_SIZE
with col2:
    if st.button("⬆️ 위쪽"):
        st.session_state.flight_pos[1] -= CELL_SIZE
    if st.button("⬇️ 아래쪽"):
        st.session_state.flight_pos[1] += CELL_SIZE
with col3:
    if st.button("➡️ 오른쪽"):
        st.session_state.flight_pos[0] += CELL_SIZE

# 총알 이동 로직
for bullet in st.session_state.bullets:
    bullet["pos"][0] += bullet["speed"][0]
    bullet["pos"][1] += bullet["speed"][1]

    # 총알이 벽에 닿으면 튕기기
    if bullet["pos"][0] <= 0 or bullet["pos"][0] >= WIDTH - CELL_SIZE:
        bullet["speed"][0] = -bullet["speed"][0]  # X축 반전
    if bullet["pos"][1] <= 0 or bullet["pos"][1] >= HEIGHT - CELL_SIZE:
        bullet["speed"][1] = -bullet["speed"][1]  # Y축 반전

    # 충돌 감지 (비행기와 총알이 닿으면 게임 오버)
    if abs(st.session_state.flight_pos[0] - bullet["pos"][0]) < CELL_SIZE and abs(st.session_state.flight_pos[1] - bullet["pos"][1]) < CELL_SIZE:
        st.error(f"💥 게임 오버! 최종 점수: {st.session_state.score}")
        st.session_state.flight_pos = [WIDTH // 2, HEIGHT - 50]  # 비행기 위치 초기화
        st.session_state.bullets = []  # 총알 초기화
        st.session_state.score = 0  # 점수 초기화
        st.session_state.frame_count = 0
        st.stop()  # 게임 멈춤

# 점수 증가
st.session_state.score += 1

# 🔫 시간이 지나면 새로운 총알 추가 (3초마다 1개씩)
st.session_state.frame_count += 1
if st.session_state.frame_count % 90 == 0:  # 3초마다 실행
    bullet_pos = [random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)]
    bullet_speed = [random.choice([-3, 3]), random.choice([-3, 3])]
    st.session_state.bullets.append({"pos": bullet_pos, "speed": bullet_speed})

# 점수 표시
st.write(f"🏆 점수: {st.session_state.score}")

# 비행기와 총알 위치 그리기 (Streamlit에서 HTML로 표시)
canvas = f'<div style="width:{WIDTH}px; height:{HEIGHT}px; background-color:black; position:relative;">'
canvas += f'<div style="width:{CELL_SIZE}px; height:{CELL_SIZE}px; background-color:{GREEN}; position:absolute; left:{st.session_state.flight_pos[0]}px; top:{st.session_state.flight_pos[1]}px;"></div>'

for bullet in st.session_state.bullets:
    canvas += f'<div style="width:{CELL_SIZE}px; height:{CELL_SIZE}px; background-color:{RED}; position:absolute; left:{bullet["pos"][0]}px; top:{bullet["pos"][1]}px;"></div>'

canvas += '</div>'
st.markdown(canvas, unsafe_allow_html=True)

# 자동 업데이트
time.sleep(speed)
st.rerun()