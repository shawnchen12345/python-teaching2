import streamlit as st

st.title("欢迎系统 👋")

name = st.text_input("请输入你的名字")
role = st.selectbox("选择角色", ["学生", "老师", "管理员"])

if name:
    st.write(f"你好 **{name}**! 欢迎来到系统。您当前的身份是: `{role}`。")
