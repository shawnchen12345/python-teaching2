import streamlit as st

# 1. 标题和文本
st.title("我的第一个 Streamlit App 🎈")
st.header("这不仅是标题，这是一个网页！")
st.write("Streamlit 是 Python 中最简单的 Web 开发框架。不需要 HTML，不需要 CSS。")

st.divider()  # 分割线

# 2. 基础交互组件
st.subheader("试着交互一下")

# 输入框
name = st.text_input("请输入你的名字", placeholder="例如: 小杜")

if name:
    st.write(f"你好，{name}！ 👋")

# 按钮
if st.button("点我庆祝"):
    st.balloons()  # 放气球特效

st.divider()

# 3. 数字与滑块
age = st.slider("你今年几岁了？", 0, 100, 18)
st.write(f"你选择了: {age} 岁")

# 4. 侧边栏 (Sidebar)
st.sidebar.title("这是侧边栏")
st.sidebar.write("这里的控件不会随着主页面滚动而消失。")
theme = st.sidebar.selectbox("选择你喜欢的主题颜色", ["红色", "蓝色", "绿色"])

st.write(f"你现在选中的主题是: {theme}")
