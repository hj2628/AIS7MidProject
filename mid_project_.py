import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import koreanize_matplotlib

st.set_page_config(
    page_title="1론_머스크",
    page_icon="🚀",
    layout="wide",
)

url = "https://raw.githubusercontent.com/hj2628/AIS7MidProject/main/2019_%E1%84%80%E1%85%AE%E1%84%86%E1%85%A2%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5_%E1%84%8B%E1%85%AF%E1%86%AF%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%91%E1%85%AE%E1%86%B7%E1%84%86%E1%85%A9%E1%86%A8%E1%84%80%E1%85%AE%E1%86%AB%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%80%E1%85%AE%E1%84%86%E1%85%A2%E1%84%8E%E1%85%AE%E1%84%8B%E1%85%B5"

url_2 = "https://raw.githubusercontent.com/hj2628/AIS7MidProject/main/2020_%E1%84%80%E1%85%AE%E1%84%86%E1%85%A2%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5_%E1%84%8B%E1%85%AF%E1%86%AF%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%91%E1%85%AE%E1%86%B7%E1%84%86%E1%85%A9%E1%86%A8%E1%84%80%E1%85%AE%E1%86%AB%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%80%E1%85%AE%E1%84%86%E1%85%A2%E1%84%8E%E1%85%AE%E1%84%8B%E1%85%B5"

url_3 = "https://raw.githubusercontent.com/hj2628/AIS7MidProject/main/20%E1%84%82%E1%85%A7%E1%86%AB%E1%84%83%E1%85%A9_%E1%84%8B%E1%85%AF%E1%86%AF%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%8F%E1%85%A9%E1%84%85%E1%85%A9%E1%84%82%E1%85%A1_%E1%84%92%E1%85%AA%E1%86%A8%E1%84%8C%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%A1%E1%84%89%E1%85%AE"

url_4 = "https://raw.githubusercontent.com/hj2628/AIS7MidProject/main/21%E1%84%82%E1%85%A7%E1%86%AB%E1%84%83%E1%85%A9_%E1%84%8B%E1%85%AF%E1%86%AF%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%8F%E1%85%A9%E1%84%85%E1%85%A9%E1%84%82%E1%85%A1_%E1%84%92%E1%85%AA%E1%86%A8%E1%84%8C%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%A1%E1%84%89%E1%85%AE"

url_5 = "https://raw.githubusercontent.com/hj2628/AIS7MidProject/main/22%E1%84%82%E1%85%A7%E1%86%AB%E1%84%83%E1%85%A9_%E1%84%8B%E1%85%AF%E1%86%AF%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%8F%E1%85%A9%E1%84%85%E1%85%A9%E1%84%82%E1%85%A1_%E1%84%92%E1%85%AA%E1%86%A8%E1%84%8C%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%A1%E1%84%89%E1%85%AE"

url_6 = "https://raw.githubusercontent.com/hj2628/AIS7MidProject/main/%E1%84%80%E1%85%A1%E1%86%AB%E1%84%91%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8_%E1%84%91%E1%85%AE%E1%86%B7%E1%84%86%E1%85%A9%E1%86%A8%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%8B%E1%85%A7%E1%86%AB%E1%84%83%E1%85%A9%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%80%E1%85%AE%E1%84%8B%E1%85%B5%E1%86%B8%E1%84%80%E1%85%A7%E1%86%BC%E1%84%92%E1%85%A5%E1%86%B7"

url_7 = "https://raw.githubusercontent.com/hj2628/AIS7MidProject/main/%E1%84%80%E1%85%A1%E1%86%AB%E1%84%91%E1%85%A7%E1%86%AB%E1%84%89%E1%85%B5%E1%86%A8_%E1%84%91%E1%85%AE%E1%86%B7%E1%84%86%E1%85%A9%E1%86%A8%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%8B%E1%85%A7%E1%86%AB%E1%84%83%E1%85%A9%E1%84%87%E1%85%A7%E1%86%AF_%E1%84%80%E1%85%AE%E1%84%8B%E1%85%B5%E1%86%B8%E1%84%87%E1%85%A7%E1%86%AB%E1%84%92%E1%85%AA"

@st.cache
def load_data(url):
    data = pd.read_csv(url)
    return data

@st.cache
def load_data(url_2):
    data_2 = pd.read_csv(url_2)
    return data_2


data = load_data(url)
data_2 = load_data(url_2)

st.markdown("## 🚀19~20년도 구매데이터🚀")

st.dataframe(data)
st.dataframe(data_2)


pxh = px.histogram(data, x="월", y="Sales_Unit", color="MasterCategoryFullName", histfunc="sum", barmode="group", title="19년 품목별 구매추이")
st.plotly_chart(pxh)


pxh = px.histogram(data_2, x="월", y="Sales_Unit", color="MasterCategoryFullName", histfunc="sum", barmode="group", title="20년 품목별 구매추이")
st.plotly_chart(pxh)

@st.cache
def load_data(url_3):
    data_3 = pd.read_csv(url_3)
    return data_3

@st.cache
def load_data(url_4):
    data_4 = pd.read_csv(url_4)
    return data_4

@st.cache
def load_data(url_5):
    data_5 = pd.read_csv(url_5)
    return data_5

data_3 = load_data(url_3)
data_4 = load_data(url_4)
data_5 = load_data(url_5)

st.markdown("## 🚀코로나19 감염현황 데이터🚀")

st.dataframe(data_3)
st.dataframe(data_4)
st.dataframe(data_5)

st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize=(15, 3))
sns.barplot(data=data_3, x="월", y="확진자수", ci=None).set_title("20년도 월별 코로나 확진자 수")
st.pyplot()

st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize=(15, 3))
sns.barplot(data=data_4, x="월", y="확진자수", ci=None).set_title("21년도 월별 코로나 확진자 수")
st.pyplot()

st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize=(15, 3))
sns.barplot(data=data_5, x="월", y="확진자수", ci=None).set_title("22년도 월별 코로나 확진자 수")
st.pyplot()

@st.cache
def load_data(url_6):
    data_6 = pd.read_csv(url_6)
    return data_6

@st.cache
def load_data(url_7):
    data_7 = pd.read_csv(url_7)
    return data_7


data_6 = load_data(url_6)
data_7 = load_data(url_7)

st.markdown("## 🚀간편식 품목별 구입경험 및 변화🚀")

st.dataframe(data_6)

st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize=(15, 5))
sns.barplot(data=data_6, x="연도", y="없음", hue="품목군").set_title("연도별 간편식 구입경험")
st.pyplot()

st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize=(15, 5))
sns.barplot(data=data_6, x="연도", y="있음", hue="품목군").set_title("연도별 간편식 구입경험")
st.pyplot()

st.dataframe(data_7)

st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize=(15, 5))
sns.barplot(data=data_7, x="연도", y="매우감소", hue="품목군").set_title("연도별 간편식 구입변화(%)")
st.pyplot()

st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize=(15, 5))
sns.barplot(data=data_7, x="연도", y="약간감소", hue="품목군").set_title("연도별 간편식 구입변화(%)")
st.pyplot()

st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize=(15, 5))
sns.barplot(data=data_7, x="연도", y="비슷", hue="품목군").set_title("연도별 간편식 구입변화(%)")
st.pyplot()

st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize=(15, 5))
sns.barplot(data=data_7, x="연도", y="약간증가", hue="품목군").set_title("연도별 간편식 구입변화(%)")
st.pyplot()

st.set_option('deprecation.showPyplotGlobalUse', False)
plt.figure(figsize=(15, 5))
sns.barplot(data=data_7, x="연도", y="매우증가", hue="품목군").set_title("연도별 간편식 구입변화(%)")
st.pyplot()
