import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

def show():
    st.write("遊び")
    
st.title('Streamlit demo')

st.write('プログレスバーの表示')
'Start!!'

#latest_iteration = st.empty()
#bar = st.progress(0)

#for i in range(100):
#    latest_iteration.text(f'Iteration {i+1}')
#    bar.progress(i+1)
#    time.sleep(0.1)

#'Done!!!!!!'

st.write('Display Image')

if st.checkbox('Show Image'):
    img = Image.open('S__64086150.jpg')
    st.image(img, caption='Kazumi Yoshii', use_column_width=True)

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1,11))
)

'あなたの好きな数字は',option ,'です'

st.write('Interactive Widgets')
text = st.text_input('あなたの趣味を教えてください')
'あなたの趣味：', text

condition = st.slider('あなたの今の調子は？', 0 ,100, 50)
'コンディション：', condition