import streamlit as st
from pages import asobi, basic, share, tenki


st.title('アプリ宿題シリーズ')
st.write('ここに宿題を置きます')

st.title("Navigation")
page = st.radio("Go to", ["asobi", "基礎", "株価可視化", "天気"])

if page == "asobi":
    asobi.show()
elif page == "基礎":
    basic.show()
elif page == "株価可視化":
    share.show()
elif page == "天気":
    tenki.show()
