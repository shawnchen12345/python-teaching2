# Streamlit 进阶教程：AI 与数据科学实战

恭喜你掌握了 Streamlit 的基础！接下来我们要挑战三个**商业级**的实战项目。

---

## 项目一：打造你的私人 GPT (AI 聊天机器人) 🤖

在这个项目中，我们将使用 Streamlit 的 `chat_message` 组件，配合 OpenAI (或者国内的模型) 打造一个网页版 ChatGPT。

### 1. 核心组件
*   `st.chat_input()`: 类似于微信底部的输入框。
*   `st.chat_message()`:用来显示一条条的消息气泡（左边是 AI，右边是你）。
*   `st.session_state.messages`: **非常重要！** 必须用列表把历史聊天记录存下来，否则 AI 会像金鱼一样，说完这句忘那句。

### 2. 代码框架 (copy to `06_chatbot.py`)
```python
import streamlit as st
import time

st.title("我的 AI 助手 🤖")

# 1. 初始化聊天记录 (Session State)
if "messages" not in st.session_state:
    st.session_state.messages = []

# 2. 展示历史消息 (每次刷新都要重新画一遍)
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 3. 处理用户输入
user_input = st.chat_input("说点什么...")

if user_input:
    # A. 显示用户的话
    with st.chat_message("user"):
        st.write(user_input)
    # 存入历史
    st.session_state.messages.append({"role": "user", "content": user_input})

    # B. AI 回复 (这里用假回复模拟，以后接 API)
    with st.chat_message("assistant"):
        response = f"你刚才说了: {user_input} (我还在学习中...)"
        st.write(response)
    # 存入历史
    st.session_state.messages.append({"role": "assistant", "content": response})
```

---

## 项目二：全能数据看板 (Data Dashboard) 📊

老板最喜欢看的界面。上传一个 Excel，自动生成由你定义的 KPIs 和图表。

### 1. 核心技能
*   `st.file_uploader()`: 让用户上传文件 (CSV/Excel)。
*   `pandas`: 读取并清洗数据。
*   `Metircs`: 顶部显示 "总销售额"、"总利润" 等大数字。
*   `Charts`: 使用 `st.bar_chart` 或更高级的 `plotly` 画图。

### 2. 代码框架 (copy to `07_dashboard.py`)
```python
import streamlit as st
import pandas as pd
import numpy as np

st.title("销售数据看板 📈")

# 1. 上传文件
uploaded_file = st.file_uploader("上传 Excel/CSV 文件", type=["csv", "xlsx"])

if uploaded_file:
    # 读取数据 (这里做个假设，实际要根据文件类型读取)
    # df = pd.read_excel(uploaded_file)
    # 为了演示，我们生成假数据
    df = pd.DataFrame(
        np.random.rand(10, 3) * 1000,
        columns=['销售额', '利润', '成本']
    )
    
    # 2. 核心指标 (KPIs)
    col1, col2, col3 = st.columns(3)
    col1.metric("总销售额", f"¥{df['销售额'].sum():.2f}")
    col2.metric("平均利润", f"¥{df['利润'].mean():.2f}")
    col3.metric("总成本", f"¥{df['成本'].sum():.2f}")

    # 3. 交互式图表
    st.subheader("销售趋势")
    st.line_chart(df)
    
    # 4. 展示原数据
    with st.expander("查看详细数据"):
        st.dataframe(df)
else:
    st.info("请上传文件以开始分析")
```

---

## 项目三：AI 图像识别 (Computer Vision) 📷

利用手机/电脑摄像头，拍一张照片，让 AI 识别里面是什么。

### 1. 核心组件
*   `st.camera_input()`: 调用摄像头拍照。
*   `st.image()`: 展示拍到的照片。
*   (进阶) `TensorFlow` / `PyTorch`:用来加载识别模型。

### 2. 代码框架 (copy to `08_camera.py`)
```python
import streamlit as st

st.title("AI 识物 (演示版) 📷")

# 1. 调用摄像头
picture = st.camera_input("拍一张照片")

if picture:
    # 2. 显示照片
    st.image(picture, caption='你刚刚拍的照片')
    
    # 3. 模拟识别过程 (假装自己在思考)
    with st.spinner('AI 正在识别中...'):
        import time
        time.sleep(2) # 假装思考 2 秒
        
    st.success("识别结果: 这可能是一个 **键盘** (置信度 88%)")
    
    # 真实开发中，这里会把 picture 传给 AI模型 (如 ResNet) 进行预测
```

---

###下一步建议
建议先从 **项目一 (聊天机器人)** 开始，因为它最能体现 Streamlit 的交互性。我们可以尝试接入真的 DeepSeek 或 OpenAI 的 API！
