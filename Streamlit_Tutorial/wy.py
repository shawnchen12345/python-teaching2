import streamlit as st
import dashscope
from http import HTTPStatus

# 1. 基础配置
dashscope.api_key = "sk-9337d140c8d54187bd5248dba0527434"

if 'my_counter' not in st.session_state:
    st.session_state.my_counter = 0

st.title('曼巴精神实验室 🐍')

# --- 原有逻辑保留 ---
name = st.text_input("请输入你的名字")
role = st.selectbox("选择你喜欢的角色", ['劳达', "出身", "学神", "劳氏"])

if role == '出身':
    st.write('fuck off')
elif role == '劳氏':
    if st.button('welcome'):
        st.balloons()
elif role == '劳达':
    st.snow()

st.write(f"你好，{name}！ 👋 欢迎来到系统。您当前的身份是 {role}。")

col1, col2 = st.columns(2)
with col1:
    st.image('https://p1.ssl.qhimgs1.com/sdr/400__/t045fa82cdc30ed428b.jpg', caption='劳达')
    if st.button('吃劳达肘击'):
        st.markdown('<span style="font-size:50px;">man!!!!</span>', unsafe_allow_html=True)
with col2:
    st.image('https://p3.ssl.qhimgs1.com/sdr/400__/t013c0b1d6619932ef9.jpg', caption='helicopter')
    if st.button('孩子们我能活下来吗？'):
        st.audio("see_you_again.mp3", format="audio/mp3", start_time=0, loop=True, autoplay=True)
        st.balloons()

if st.button('点赞复活劳大'):
    st.session_state.my_counter += 1
st.metric(label="当前点赞数", value=st.session_state.my_counter)

if st.session_state.my_counter >= 24: # 科比球号 24
    st.write("Mamba Out, but never forgotten. 🏀")

st.divider()

# --- 新增聊天机器人逻辑 (科比版) ---
st.subheader("🏀 与科比对话 (Mamba Chat)")

# 初始化消息，加入 System Prompt 设定角色
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "你现在是科比·布莱恩特（Kobe Bryant）。你说话富有激励性，充满曼巴精神。你的回答应该简短、有力，常用‘凌晨四点的洛杉矶’、‘永不言弃’等梗。你要称呼对方为‘朋友’或‘伙计’。"}
    ]

# 显示历史对话（跳过 system 消息）
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# 聊天输入
prompt = st.chat_input("伙计，你想聊点什么？")

if prompt:
    # 显示用户消息
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调用 API
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            response = dashscope.Generation.call(
                model=dashscope.Generation.Models.qwen_turbo,
                messages=st.session_state.messages,
                result_format='message',
                stream=True,
                incremental_output=True
            )

            for chunk in response:
                if chunk.status_code == HTTPStatus.OK:
                    content = chunk.output.choices[0]['message']['content']
                    full_response += content
                    message_placeholder.markdown(full_response + "▌")
                else:
                    st.error(f'曼巴能量中断: {chunk.message}')
            
            message_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            st.error(f"发生错误: {e}")
