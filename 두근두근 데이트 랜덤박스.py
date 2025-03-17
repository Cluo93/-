import random
import streamlit as st

def get_random_choice(category, choices):
    return random.choice(choices)

st.title("💖 두근두근 랜덤 데이트 박스 💖")

date_places = ["강남", "홍대", "이태원", "성수", "잠실", "건대", "압구정 로데오", "서울숲", "용산", "코엑스", "왕십리", "수서", "청량리💖", "고터"]
missions = ["손잡고 1시간 걷기 🚶‍♂️🚶‍♀️", "길거리 음식 3개 먹기 🍡", "민경이가 좋아하는 음식 먹기 🍣", "민승이가 좋아하는 음식 먹기 🍣", "사진 5장 이상 찍기 📸", "민경이가 요리해서 같이먹기", "민승이가 요리해서 같이먹기"]
food_choices = ["한식", "양식", "일식", "중식"]
movie_genres = ["로맨스", "스릴러", "코미디", "SF", "액션", "드라마"]
special_events = ["민경이가 원하는 거 다 들어주기", "민경이한테 깜짝 선물 주기", "민승이한테 볼 뽀뽀해주기", "민승이한테 사랑해 하면서 안아주기", "민승이가 원하는 거 다 들어주기", "민승이한테 깜짝 선물 주기", "민경이한테 볼 뽀뽀해주기", "민경이한테 사랑해 하면서 안아주기", "민경이 장점 3가지 얘기하기", "민승이 장점 3가지 얘기하기"]

if st.button("🎡 데이트 장소 랜덤박스"):
    st.success(get_random_choice("데이트 장소", date_places))

if st.button("🎯 미션 랜덤박스"):
    st.success(get_random_choice("미션", missions))

if st.button("🍽️ 음식 랜덤박스"):
    st.success(get_random_choice("음식/카페", food_choices))

if st.button("🎬 영화 랜덤박스"):
    st.success(get_random_choice("영화 장르", movie_genres))

if st.button("🎁 특별 이벤트 랜덤박스"):
    st.success(get_random_choice("특별 이벤트", special_events))

st.markdown("### ✨ 민경이가 데이트 하고 싶을때 뽑기 ✨")
st.markdown("### ✨ 다시 뽑고 싶을땐 '사랑해' 라고 말하기 ✨")