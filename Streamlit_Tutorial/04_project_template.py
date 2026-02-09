import streamlit as st

st.set_page_config(page_title="任务管理器", page_icon="✅", layout="wide")

# 初始化 Session State
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# ================================
# 1. 侧边栏: 添加新任务
# ================================
st.sidebar.header("添加新任务")

new_task = st.sidebar.text_input("任务名称", placeholder="例如: 完结 Streamlit 教程")
priority = st.sidebar.select_slider("优先级", options=["低", "中", "高"], value="中")

if st.sidebar.button("添加任务"):
    if new_task:
        # 提示: 将任务作为一个字典添加到 st.session_state.tasks 列表中
        # 任务字典结构: {'name': new_task, 'priority': priority, 'done': False}
        pass  # TODO: 删除 pass，写你的代码
        st.success("添加成功！")
    else:
        st.error("任务名不能为空！")

# ================================
# 2. 主区域: 任务列表
# ================================
st.title("我的任务清单 📝")

# 统计信息
total_tasks = len(st.session_state.tasks)
st.metric("总任务数", total_tasks)

st.divider()

# 显示任务
# 提示: 使用 for 循环遍历 st.session_state.tasks
# 提示: 使用 st.checkbox 来显示任务，并将 checkbox 的状态绑定到 task['done']
if not st.session_state.tasks:
    st.info("暂无任务，快去左侧添加吧！")
else:
    for i, task in enumerate(st.session_state.tasks):
        # 每一行显示一个任务
        col1, col2 = st.columns([0.8, 0.2])
        
        with col1:
            # TODO: 使用 st.checkbox 显示任务名
            pass
            
        with col2:
            st.write(f"优先级: {task['priority']}")

st.divider()

# ================================
# 3. 清理功能
# ================================
if st.button("清除已完成任务"):
    # TODO: 过滤掉 done 为 True 的任务
    st.rerun()
