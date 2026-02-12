import streamlit as st

st.title("简易计算器 🧮")

col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("数字 1", value=0.0)
with col2:
    num2 = st.number_input("数字 2", value=0.0)

operation = st.radio("选择运算", ["加", "减", "乘", "除"], horizontal=True)

if st.button("开始计算"):
    result = 0
    if operation == "加":
        result = num1 + num2
    elif operation == "减":
        result = num1 - num2
    elif operation == "乘":
        result = num1 * num2
    elif operation == "除":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("错误: 不能除以零！")
            st.stop()  # 停止后续代码执行
    
    st.success(f"结果是: {result}")
