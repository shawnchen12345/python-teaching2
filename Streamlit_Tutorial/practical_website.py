'''import streamlit as st
col1,col2,col3=st.columns(3)
with col1:  
    num1=st.text_input('',value=0)
    num1=float(num1)
with col2:
    op=st.radio('请输入你想要的符号',['+','-',"x",'/'])
with col3:
    num2=st.text_input("  ",value=0)
    num2=float(num2)
   
if op=="+":
    result=num1+num2
elif op=="-":
    result=num1-num2
elif op=='x':
    result=num1*num2
elif op=='/' and num2!=0:
    result=num1/num2
st.success(f'{result}')'''
import streamlit as st
import pandas as pd
import numpy as np
a={"数学": 85, "英语": 78, "物理": 92}
df = pd.DataFrame(a)
st.datafream(df)










