import streamlit as st
col1, col2, col3 = st.columns(3)
# 1. 简单显示
col1.metric(label="当前温度", value="26 °C")
# 2. 带涨跌 (自动变色)
# delta 是正数 -> 绿色箭头 (涨)
col2.metric(label="股票价格", value="$128.50", delta="1.25")
# 3. 带跌幅 (自动变色)
# delta 是负数 -> 红色箭头 (跌)
col3.metric(label="剩余电量", value="15%", delta="-5%")