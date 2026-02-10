import streamlit as st
import dashscope
from http import HTTPStatus

dashscope.api_key = "sk-9337d140c8d54187bd5248dba0527434"

st.title("🌐 AI 翻译官")

text_in = st.text_area("请输入要翻译的中文内容:")

if st.button("开始翻译"):
    if text_in:
        with st.spinner("翻译中..."):
            # 构造提示词
            prompt = f"请将以下内容翻译成地道的英文，只输出翻译结果：\n{text_in}"
            
            response = dashscope.Generation.call(
                model=dashscope.Generation.Models.qwen_turbo,
                prompt=prompt
            )
            
            if response.status_code == HTTPStatus.OK:
                result = response.output.text
                st.success("翻译结果：")
                st.write(result)
            else:
                st.error(f"出错啦: {response.message}")
    else:
        st.warning("内容不能为空内容哦")