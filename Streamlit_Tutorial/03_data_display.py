import streamlit as st
import pandas as pd
import numpy as np

st.title("数据可视化 📊")

# 1. 展示表格
st.subheader("1. 数据表格")

data = {
    '姓名': ['张三', '李四', '王五', '赵六'],
    '语文': [88, 92, 75, 82],
    '数学': [95, 78, 88, 90],
    '英语': [85, 95, 82, 88]
}
df = pd.DataFrame(data)

# st.dataframe 支持交互（排序、搜索），st.table 是静态表格
st.dataframe(df, use_container_width=True)

# 2. 简单的图表
st.subheader("2. 绘制图表")

# 柱状图
st.bar_chart(df.set_index('姓名'))

# 折线图 (模拟股票走势)
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A公司', 'B公司', 'C公司']
)
st.line_chart(chart_data)

# 3. 交互式图表体验
st.subheader("3. 动态调整")
number = st.slider("调整数据量", 10, 100, 20)
random_df = pd.DataFrame(np.random.randn(number, 2), columns=['x', 'y'])
st.area_chart(random_df)
