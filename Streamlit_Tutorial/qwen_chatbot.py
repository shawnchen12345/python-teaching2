import streamlit as st
import dashscope
from http import HTTPStatus

st.title("Qwen AI 助手 (通义千问) 🤖")

# ==========================================
# 0. 获取 API Key (非常重要!)
# ==========================================
# 为了安全，这里建议把它放在 secrets.toml 或者环境变量
# 临时测试可以填这里，但切记不要上传到 GitHub
my_api_key = "sk-9337d140c8d54187bd5248dba0527434"  # 请替换你的 Key
dashscope.api_key = my_api_key

# ==========================================
# 1. 初始化聊天记录
# ==========================================
if "messages" not in st.session_state:
    st.session_state.messages = []
    # 可以加个开场白
    st.session_state.messages.append(
        {'role': 'assistant', 'content': '你好！我是通义千问 Qwen，有什么可以帮你的吗？'}
    )

# ==========================================
# 2. 展示历史消息 (每次刷新，把对话记录画出来)
# ==========================================
for msg in st.session_state.messages:
    if msg['role'] == 'user':
        st.chat_message("user").write(msg['content'])
    else:
        st.chat_message("assistant").write(msg['content'])

# ==========================================
# 3. 处理用户输入
# ==========================================
prompt = st.chat_input("问我任何问题...")

if prompt:
    # A. 显示并保存用户问题
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({'role': 'user', 'content': prompt})

    # B. 调用 Qwen API (核心部分)
    # 使用 dashscope.Generation.call
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # 流式输出 (stream=True) 会更有感觉
            response = dashscope.Generation.call(
                model=dashscope.Generation.Models.qwen_turbo,
                messages=st.session_state.messages,
                result_format='message',  # 设置结果格式为 message
                stream=True,     # 开启流式输出
                incremental_output=True  # 增量输出模式
            )

            # 处理流式响应
            for chunk in response:
                if chunk.status_code == HTTPStatus.OK:
                    content = chunk.output.choices[0]['message']['content']
                    full_response += content
                    message_placeholder.markdown(full_response + "▌")
                else:
                    st.error(f'请求失败: {chunk.code} - {chunk.message}')
            
            # 显示最终结果 (去掉光标)
            message_placeholder.markdown(full_response)
            
            # C. 保存 AI 回复到历史记录
            st.session_state.messages.append({'role': 'assistant', 'content': full_response})

        except Exception as e:
            st.error(f"发生错误: {e}")
