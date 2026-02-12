import streamlit as st

st.set_page_config(page_title="任务管理器", page_icon="✅", layout="wide")

# 初始化 Session State
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# ================================
# 1. 侧边栏: 添加新任务
# ================================
st.sidebar.header("添加新任务")
new_task = st.sidebar.text_input("任务名称")
priority = st.sidebar.select_slider("优先级", options=["低", "中", "高"], value="中")

if st.sidebar.button("添加任务"):
    if new_task:
        # 添加任务字典
        st.session_state.tasks.append({
            'name': new_task,
            'priority': priority,
            'done': False
        })
        st.success("添加成功！")
        st.rerun()
    else:
        st.error("请输入任务名称")

# ================================
# 2. 主区域: 任务列表
# ================================
st.title("我的任务清单 📝")

# 统计
pending_count = len([t for t in st.session_state.tasks if not t['done']])
total_count = len(st.session_state.tasks)

col1, col2 = st.columns(2)
col1.metric("待办任务", pending_count)
col2.metric("总任务", total_count)

# 进度条
if total_count > 0:
    progress = (total_count - pending_count) / total_count
    st.progress(progress)
else:
    st.progress(0.0)

st.divider()

if not st.session_state.tasks:
    st.info("暂无任务")
else:
    # 必须使用 enumerate 才能定位并修改对应的任务
    for i, task in enumerate(st.session_state.tasks):
        col_check, col_info = st.columns([0.1, 0.9])
        
        with col_check:
            # 绑定 checkbox 状态到 session_state (需要手动处理或者直接更新)
            # 这里我们使用 key 来区分不同的 checkbox
            is_done = st.checkbox("", value=task['done'], key=f"task_{i}")
            # 更新状态
            st.session_state.tasks[i]['done'] = is_done
            
        with col_info:
            task_name = task['name']
            prio = task['priority']
            
            # 样式处理
            if is_done:
                st.markdown(f"~~{task_name}~~ (优先级: {prio})")
            else:
                # 高优先级加粗显示
                if prio == "高":
                    st.markdown(f"🔥 **{task_name}**")
                else:
                    st.write(f"{task_name} ({prio})")

st.divider()

# 清理功能
if st.button("🗑️ 清除已完成任务"):
    # 保留未完成的任务 (列表推导式)
    st.session_state.tasks = [t for t in st.session_state.tasks if not t['done']]
    st.rerun()
