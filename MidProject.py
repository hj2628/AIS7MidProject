import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import koreanize_matplotlib

st.set_page_config(
    page_title="1론머스크 MidProject",
    page_icon="🚀",
    layout="wide",
)

st.markdown("# 🚀1론머스크🚀")
st.sidebar.markdown("# 공공데이터")

url = ["https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis3_19.csv"
, "https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis3_20.csv"
, "https://raw.githubusercontent.com/chihyuns0ng/AIS7MidProject/main/data/kosis3_21.csv"
]

# @st.cache
# url_load_state = st.text('Loading data...')

kosis3_19=pd.read_csv(url[0])
kosis3_20=pd.read_csv(url[1])
kosis3_21=pd.read_csv(url[2])

# url_load_state.text("Done! (using st.cache)")

kosis3_19_number = kosis3_19[1:6].drop("특성별(1)", axis=1)
kosis3_20_number = kosis3_20[1:6].drop("특성별(1)", axis=1)
kosis3_21_number = kosis3_21[1:5].drop("특성별(1)", axis=1)

kosis3_19_number = kosis3_19_number.set_index("특성별(2)")
kosis3_19_number = kosis3_19_number.rename_axis("가구원수")
kosis3_20_number = kosis3_20_number.set_index("특성별(2)")
kosis3_20_number = kosis3_20_number.rename_axis("가구원수")
kosis3_21_number = kosis3_21_number.set_index("특성별(2)")
kosis3_21_number = kosis3_21_number.rename_axis("가구원수")

fig, ax = plt.subplots()
kosis3_19_number.T[:-2].plot(kind="bar", figsize=(20,10),fontsize=15, rot=20)
_ = plt.title("2019년 가구원수별", fontsize=20)
_ = plt.legend(fontsize=20, bbox_to_anchor=(1.2,1))
st.pyplot(fig)

# st.dataframe(kosis3_19_number)
