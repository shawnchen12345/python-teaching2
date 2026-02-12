import streamlit as st
import pandas as pd

st.title("班级成绩可视化 📊")

# 原始数据
raw_data = {"数学": 85, "英语": 78, "物理": 92, "化学": 88}

# 侧边栏滑块
adjustment = st.slider("全员加分/减分", -20, 20, 0)

# 处理数据
# 将字典转换为 DataFrame 以便绘图
# 注意: 我们需要根据 adjustment 动态修改分数
adjusted_data = {}
for subject, score in raw_data.items():
    new_score = score + adjustment
    # 限制分数在 0-100 之间 (可选)
    new_score = max(0, min(100, new_score))
    adjusted_data[subject] = new_score

# 转换为 DataFrame (Streamlit 图表通常需要 DataFrame)
df = pd.DataFrame(list(adjusted_data.items()), columns=["科目", "分数"])

st.subheader("当前分数表")
st.dataframe(df)

st.subheader("分数柱状图")
st.bar_chart(df.set_index("科目"))
