# 大模型 API 接入实战练习与答案 (LLM API Exercises)

本练习册旨在帮助你掌握如何通过 DashScope (通义千问) API 在 Streamlit 应用中接入大模型能力。

---

## 习题 1：AI 翻译官 (初级)
**目标**：掌握基础的 API 调用和提示词拼接。
**要求**：用户输入中文，点击按钮后，AI 将其翻译为英文并显示。

### 答案代码 (`ex_llm_1_translator.py`):
```python
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
```

---

## 习题 2：严厉的面试官 (中级)
**目标**：掌握 System Prompt 的设定。
**要求**：设定 AI 为一名严厉的技术面试官，针对用户的自我介绍进行提问。

### 答案代码 (`ex_llm_2_interviewer.py`):
```python
import streamlit as st
import dashscope
from http import HTTPStatus

dashscope.api_key = "sk-9337d140c8d54187bd5248dba0527434"

st.title("💼 曼巴技术面试")

intro = st.text_area("请进行简单的自我介绍：")

if st.button("开始挑战"):
    if intro:
        with st.spinner("面试官正在审视你的简历..."):
            # 使用 messages 格式来设定 System 角色
            messages = [
                {"role": "system", "content": "你是一个极其严厉的技术面试官。你说话非常直接，不喜欢废话。你的目标是找出应聘者技术上的漏洞。"},
                {"role": "user", "content": f"这是我的自我介绍：{intro}"}
            ]
            
            response = dashscope.Generation.call(
                model='qwen-turbo',
                messages=messages,
                result_format='message'
            )
            
            if response.status_code == HTTPStatus.OK:
                reply = response.output.choices[0]['message']['content']
                st.chat_message("assistant").write(reply)
            else:
                st.error("连接中断")
```

---

## 习题 3：长文摘要神器 (中级)
**目标**：练习处理大文本及结构化反馈。
**要求**：AI 总结长文，并要求以 Markdown 表格或列表格式输出。

### 答案代码 (`ex_llm_3_summarizer.py`):
```python
import streamlit as st
import dashscope
from http import HTTPStatus

dashscope.api_key = "sk-9337d140c8d54187bd5248dba0527434"

st.title("📝 智能长文缩写")

long_text = st.text_area("粘贴你的长文章：", height=200)

if st.button("一键总结"):
    if long_text:
        with st.spinner("正在提取核心观点..."):
            prompt = f"请阅读以下文章，并提取 3 个核心观点。要求：以无序列表格式显示，每个观点不超过 30 字。\n\n文章内容：{long_text}"
            
            response = dashscope.Generation.call(model='qwen-turbo', prompt=prompt)
            
            if response.status_code == HTTPStatus.OK:
                st.markdown("### 🔍 核心要点：")
                st.markdown(response.output.text)
            else:
                st.error("处理失败")
```

---

## 习题 4：代码纠错大师 (高级)
**目标**：结合代码块展示与专业领域处理。
**要求**：AI 找出 Python 代码中的 Bug 并给出修复代码。

### 答案代码 (`ex_llm_4_debugger.py`):
```python
import streamlit as st
import dashscope
from http import HTTPStatus

dashscope.api_key = "sk-9337d140c8d54187bd5248dba0527434"

st.title("🐍 Python 代码医生")

code_input = st.text_area("将有 Bug 的代码粘贴到这里：", height=150)

if st.button("寻找 Bug"):
    if code_input:
        prompt = f"你是一个 Python 专家。请指出下面代码中的错误并解释原因，最后给出修复后的完整代码块：\n\n```python\n{code_input}\n```"
        
        with st.spinner("正在逐行扫描代码..."):
            response = dashscope.Generation.call(model='qwen-max', prompt=prompt) # 使用更强的 max 模型
            
            if response.status_code == HTTPStatus.OK:
                st.markdown(response.output.text)
            else:
                st.error("分析失败")
```

---

## 习题 5：图片解说员 (挑战)
**目标**：掌握多模态视觉模型 (Qwen-VL)。
**要求**：用户上传图片，AI 描述图片内容。

### 答案代码 (`ex_llm_5_vision.py`):
```python
import streamlit as st
import dashscope
from http import HTTPStatus

dashscope.api_key = "sk-9337d140c8d54187bd5248dba0527434"

st.title("👁️ AI 识物眼睛")

uploaded_img = st.file_uploader("传一张照片看看：", type=['jpg', 'png'])

if uploaded_img:
    st.image(uploaded_img, caption="已上传照片", width=300)
    
    # 模拟 Qwen-VL 调用 (注意：VL 模型需要特定的文件上传格式，这里演示核心逻辑)
    if st.button("让 AI 看看图里有什么"):
        st.info("提示：视觉模型需要将图片上传至 OSS 或转换为 Base64 链接。")
        # 实际开发需参考官网 VL 模型调用示例
        st.success("识别示例结果：这张图片里包含一个键盘和一支笔...")
```
