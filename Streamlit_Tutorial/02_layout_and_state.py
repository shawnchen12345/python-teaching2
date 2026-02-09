import streamlit as st

st.title("布局与状态管理 🧠")

# ==========================================
# Part 1: 布局 (Layouts)
# ==========================================
st.header("1. 页面布局")

# 多列布局 columns
col1, col2 = st.columns(2)

with col1:
    st.image("https://static.streamlit.io/examples/cat.jpg", caption="猫猫")
    if st.button("给猫点赞"):
        st.write("喵！🐱")

with col2:
    st.image("https://static.streamlit.io/examples/dog.jpg", caption="狗狗")
    if st.button("给狗点赞"):
        st.write("汪！🐶")

# 选项卡 tabs
tab1, tab2 = st.tabs(["基本信息", "详细介绍"])
with tab1:
    st.write("这里是基本信息...")
with tab2:
    st.write("这里是更多详细的内容...")


st.divider()

# ==========================================
# Part 2: 状态 (Session State)
# ==========================================
st.header("2. 核心难点: 会话状态 (Session State)")

st.info("试着点击下面的普通按钮，你会发现它无法记住点击次数，因为每次点击都会重运行整个脚本，变量由 0 重新开始。")

# 错误示范
count = 0
if st.button("普通按钮 (+1)"):
    count += 1
st.write(f"普通计数: {count}")

st.success("下面是使用了 session_state 的按钮，它可以'记住'之前的状态！")

# 正确示范：初始化状态
if 'my_counter' not in st.session_state:
    st.session_state.my_counter = 0

# 增加计数
if st.button("记忆按钮 (+1)"):
    st.session_state.my_counter += 1

st.metric(label="当前计数", value=st.session_state.my_counter)

if st.button("重置"):
    st.session_state.my_counter = 0
    st.rerun()  # 强制刷新页面
