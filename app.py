import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 페이지 기본 설정
st.set_page_config(
    page_title="CSV 데이터 시각화 도구",
    page_icon="📊",
    layout="wide"
)

def main():
    # 타이틀 설정
    st.title("📊 CSV 데이터 시각화 도구")
    st.write("CSV 파일을 업로드하면 데이터를 시각화해 드립니다.")

    # 파일 업로드 위젯
    uploaded_file = st.file_uploader("CSV 파일을 업로드하세요.", type=["csv"])

    if uploaded_file is not None:
        try:
            # 데이터 로드
            df = pd.read_csv(uploaded_file)
            
            # 데이터 미리보기
            st.subheader("데이터 미리보기")
            st.dataframe(df.head())
            
            # 데이터 기본 정보
            st.subheader("데이터 기본 정보")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("총 행 개수", df.shape[0])
            with col2:
                st.metric("총 열 개수", df.shape[1])
            with col3:
                st.write("결측치 요약:")
                st.write(df.isnull().sum()[df.isnull().sum() > 0])
                
            # 사이드바 시각화 설정
            st.sidebar.header("시각화 설정")
            
            # 숫자형 컬럼만 필터링 (시각화에 사용하기 위함)
            numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
            all_columns = df.columns.tolist()
            
            if len(all_columns) >= 2:
                # X, Y축 선택
                x_axis = st.sidebar.selectbox("X축 선택", all_columns)
                # Y축은 숫자형 데이터만 권장하지만 전체 선택 가능하게 함
                y_axis = st.sidebar.selectbox("Y축 선택", all_columns, index=1 if len(all_columns) > 1 else 0)
                
                # 그래프 종류 선택
                plot_type = st.sidebar.selectbox(
                    "그래프 종류 선택",
                    ["산점도 (Scatter Plot)", "선 그래프 (Line Chart)", "막대 그래프 (Bar Chart)"]
                )
                
                st.subheader(f"{x_axis} vs {y_axis} ({plot_type})")
                
                # Matplotlib Figure 생성
                fig, ax = plt.subplots(figsize=(10, 6))
                
                try:
                    # 선택된 그래프 종류에 따라 그리기
                    if plot_type == "산점도 (Scatter Plot)":
                        sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax)
                    elif plot_type == "선 그래프 (Line Chart)":
                        sns.lineplot(data=df, x=x_axis, y=y_axis, ax=ax)
                    elif plot_type == "막대 그래프 (Bar Chart)":
                        # 막대 그래프는 데이터가 너무 많으면 보기 어려우므로 상위 50개만 표시
                        if len(df) > 50:
                            st.warning("데이터가 50개를 초과하여 상위 50개만 막대 그래프로 표시합니다.")
                            sns.barplot(data=df.head(50), x=x_axis, y=y_axis, ax=ax)
                        else:
                            sns.barplot(data=df, x=x_axis, y=y_axis, ax=ax)
                            
                    # X축 라벨 회전 (글자가 겹치는 것 방지)
                    plt.xticks(rotation=45, ha='right')
                    plt.tight_layout()
                    
                    # Streamlit에 그래프 표시
                    st.pyplot(fig)
                    
                except Exception as e:
                    st.error(f"그래프를 그리는 중 오류가 발생했습니다: {e}")
                    st.info("선택한 컬럼의 데이터 타입이 해당 그래프와 맞지 않을 수 있습니다.")
                    
            else:
                st.warning("데이터 시각화를 위해서는 최소 2개 이상의 열이 필요합니다.")
                
            # 데이터 통계 요약
            if len(numeric_columns) > 0:
                st.subheader("데이터 통계 요약 (숫자형 데이터)")
                st.dataframe(df[numeric_columns].describe())
                
        except pd.errors.EmptyDataError:
            st.error("빈 CSV 파일입니다.")
        except pd.errors.ParserError:
            st.error("CSV 파일을 파싱하는 데 오류가 발생했습니다. 파일 형식을 확인해주세요.")
        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")
            
    else:
        st.info("분석을 시작하려면 왼쪽 메뉴나 위의 '찾아보기' 버튼을 통해 CSV 파일을 업로드해주세요.")

if __name__ == "__main__":
    main()
