import streamlit as st
col1,col2,col3=st.columns(3)
with col1:  
    num1=st.text_input('',value=int(0))
with col2:
    op=st.radio('请输入你想要的符号',['+','-',"x",'/'])
with col3:
    num2=st.text_input("  ",value=int(0))
if op=="+":
    result=num1+num2
elif op=="-":
    result=num1-num2
elif op=='x':
    result=num1*num2
else:
    result=num1/num2
st.success(f'{result}')








