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
if 'task_basket' not in st.session_state:
    st.session_state.task_basket = []
st.sidebar.title("任务表")
n_task=st.sidebar.text_input('请添加任务')
priority=st.sidebar.select_slider("优先级", options=['low','mid','high'])




if st.sidebar.button('sent'):

    
    new_item={'任务':[n_task],'优先级':[priority],'完成状态':'no'}
    st.session_state.task_basket.append(new_item)
    df=pd.DataFrame(st.session_state.task_basket)
    st.dataframe(df)
    edited_df=st.dataeditor(df,column_config={'已完成':st.column_config.CheckboxColumn('任务状态'),help='点击勾选完成任务',default=False})
   

    









