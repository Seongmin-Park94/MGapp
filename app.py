import streamlit as st
import streamlit.components.v1 as components

# 1. HTML 코드를 문자열로 읽어오거나 정의합니다.
# (파일에서 읽어오는 것을 권장합니다.)
with open("team_budget_dashboard.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# 2. components.html을 사용하여 렌더링합니다.
# 높이(height)를 충분히 주어야 스크롤 없이 볼 수 있습니다.
components.html(html_content, height=1200, scrolling=True)
