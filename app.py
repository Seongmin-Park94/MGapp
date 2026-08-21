import streamlit as st
import requests
from streamlit_lottie import st_lottie

# Lottie URL을 불러오는 함수 (오류 발생 시 앱이 멈추지 않도록 예외 처리 추가)
def load_lottieurl(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception as e:
        return None

st.title("Hello 성민 👋")
st.markdown("풍선입니다! 🎈")

# Lottie 풍선 애니메이션 URL (안정적인 링크로 교체)
lottie_balloons_url = "https://assets9.lottiefiles.com/packages/lf20_p8bfn5to.json"

# 애니메이션 데이터 불러오기
lottie_balloons = load_lottieurl(lottie_balloons_url)

# 데이터가 성공적으로 불러와졌다면 화면에 렌더링
if lottie_balloons:
    st_lottie(lottie_balloons, height=400, key="infinite_balloons")
else:
    # 링크가 만료되었거나 인터넷 문제로 불러오지 못했을 때 띄울 에러 메시지
    st.error("앗! 풍선 애니메이션을 불러오지 못했습니다. Lottie URL 링크가 유효한지 확인해 주세요.")
