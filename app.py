import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Lottie 애니메이션을 불러오는 함수
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.title("Hello Streamlit-er 👋")
st.markdown(
    """ 
    This is a playground for you to try Streamlit and have fun. 

    **There's :rainbow[so much] you can build!**
    """
)

# 로딩 시 풍선 한 번 띄우기 (기본 기능)
st.balloons()

st.markdown("### ✨ 추가된 고해상도 무한 애니메이션 ✨")

# 1. 우주비행사 애니메이션 (Lottie URL)
lottie_url = "https://lottie.host/9e4bdc80-cbe0-4ef0-94dc-215f6fc50a58/tA7F87T9kI.json"
lottie_json = load_lottieurl(lottie_url)

# 2. 화면에 애니메이션 렌더링 (버튼 없이 무한 반복됨)
if lottie_json:
    st_lottie(lottie_json, height=300, key="space_animation")
