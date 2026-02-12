import streamlit as st

st.title("持久化计数器 🔢")

# 1. 初始化 Session State
if 'count' not in st.session_state:
    st.session_state.count = 0

# 2. 显示当前数值
st.metric(label="当前计数", value=st.session_state.count)

# 3. 按钮操作
col1, col2, col3 = st.columns([1, 1, 3])

with col1:
    if st.button("➕ 增加"):
        st.session_state.count += 1
        st.rerun()  # 刷新页面以立即更新界面

with col2:
    if st.button("➖ 减少"):
        st.session_state.count -= 1
        st.rerun()

with col3:
    if st.button("❌ 重置"):
        st.session_state.count = 0
        st.rerun()
