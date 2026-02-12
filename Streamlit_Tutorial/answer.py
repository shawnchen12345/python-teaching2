import streamlit as st

st.set_page_config(page_title="任务管理器", page_icon="✅", layout="wide")

# 初始化 Session State
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# ================================
# 1. 侧边栏: 添加新任务
# ================================
st.sidebar.header("添加新任务")
new_task_name = st.sidebar.text_input("任务名称")
prio_level = st.sidebar.select_slider("优先级", options=["低", "中", "高"], value="中")

if st.sidebar.button("添加任务"):
    if new_task_name:
        # 添加任务字典 (状态默认为未完成: done=False)
        st.session_state.tasks.append({
            'name': new_task_name,
            'priority': prio_level,
            'done': False
        })
        st.success("添加成功！")
        st.rerun() # 立即刷新界面
    else:
        st.sidebar.error("请输入任务名称")

# ================================
# 2. 主区域: 任务列表展示
# ================================
st.title("我的任务清单 📝")

# 统计数据
pending_count = len([t for t in st.session_state.tasks if not t['done']])
total_count = len(st.session_state.tasks)

c1, c2 = st.columns(2)
c1.metric("待办任务", pending_count)
c2.metric("总任务", total_count)

# 进度条
if total_count > 0:
    progress = (total_count - pending_count) / total_count
    st.progress(progress)
else:
    st.progress(0.0)

st.divider()

# --- 关键部分：使用 enumerate 显示列表 ---
if not st.session_state.tasks:
    st.info("目前还没有任务，请在侧边栏添加一个吧！")
else:
    # 遍历列表中的每一个任务字典
    for i, task in enumerate(st.session_state.tasks):
        # 创建两列：一列放勾选框，一列放文字
        col_check, col_info = st.columns([0.1, 0.9])
        
        with col_check:
            # 关键修复：label 不能为空，但可以用 label_visibility 隐藏
            # 使用 key=f"task_{i}" 确保每个勾选框都是唯一的
            is_done = st.checkbox(
                "完成", 
                value=task['done'], 
                key=f"check_{i}", 
                label_visibility="collapsed"
            )
            # 实时同步勾选状态到内存
            st.session_state.tasks[i]['done'] = is_done
            
        with col_info:
            name = task['name']
            prio = task['priority']
            
            # 如果勾选了，文字显示删除线样式
            if is_done:
                st.markdown(f"~~{name}~~ <font color='gray'>(已完成)</font>", unsafe_allow_html=True)
            else:
                # 根据优先级显示不同样式
                if prio == "高":
                    st.markdown(f"🔥 **{name}** (优先级: {prio})")
                else:
                    st.write(f"{name} (优先级: {prio})")

st.divider()

# 侧边栏底部清理功能
if st.button("🗑️ 清除所有已完成任务"):
    st.session_state.tasks = [t for t in st.session_state.tasks if not t['done']]
    st.rerun()
