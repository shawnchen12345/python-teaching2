import dashscope
from dashscope import ImageSynthesis
import streamlit as st

# 使用你之前在 qwen_chatbot.py 中填写的正确 Key
dashscope.api_key = "sk-9337d140c8d54187bd5248dba0527434"

def generate_image(prompt):
    # wanx_v1 是通义万相模型
    rsp = ImageSynthesis.call(model=ImageSynthesis.Models.wanx_v1,
                              prompt=prompt,
                              n=1,
                              size='1024*1024')
    if rsp.status_code == 200:
        return rsp.output.results[0].url
    else:
        st.error(f"接口返回错误码: {rsp.code} - {rsp.message}")
        return None

st.title("AI 绘画大师 (通义万相) 🎨")
st.info("提示：AI 绘画较慢，点击后请等待约 10-20 秒。")

prompt = st.text_input("描述你想要的画面 (建议中文):", "一只穿着宇航服在火星上吃火锅的熊猫")

if st.button("开始绘画"):
    with st.spinner("AI 正在构思并绘画中，请稍候..."):
        url = generate_image(prompt)
        if url:
            st.image(url, caption=f"生成结果: {prompt}", use_column_width=True)
            st.success("绘画完成！")
        else:
            st.error("生成失败，请检查 API Key 是否有效。")