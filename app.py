import streamlit as st
import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.title("Hello Streamlit-er 👋")
st.markdown("로딩이나 버벅거림 없이 무한으로 날아다니는 풍선입니다! 🎈")

# Lottie 풍선 애니메이션 URL
lottie_balloons_url = "https://lottie.host/932ed212-e8ef-4680-8772-2ff85f523c9f/X6J7M0Pz8F.json"
lottie_balloons = load_lottieurl(lottie_balloons_url)

if lottie_balloons:
    # 앱 한가운데에 무한 반복되는 풍선 띄우기
    st_lottie(lottie_balloons, height=400, key="infinite_balloons")
