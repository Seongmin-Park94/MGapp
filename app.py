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

st.title("Hello Streamlit-er 👋")
st.markdown("로딩이나 버벅거림 없이 무한으로 날아다니는 풍선입니다! 🎈")

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

st.markdown("---")

# 이미지 불러오기 (주의: 실제 깃허브에 올려진 파일의 확장자 .png / .jpg 와 정확히 일치해야 합니다)
try:
    # 화면 너비에 맞춰서 이미지를 예쁘게 출력합니다.
    st.image("image1.jpg", caption="image1", use_container_width=True)
except Exception as e:
    # 파일명이나 확장자가 달라서 이미지를 못 찾을 경우 띄워줄 안내 메시지
    st.warning("이미지를 찾을 수 없습니다. 깃허브에 저장된 파일 이름이 'image1.png'인지, 아니면 'image1.jpg'인지 확장자를 꼭 확인해 주세요!")
