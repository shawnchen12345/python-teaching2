import streamlit as st

# markdown
st.markdown('Streamlit is **_really_ cool**.')

# 设置网页标题
st.title('This is a title')

# 展示一级标题
st.header('This is a header')

# 展示二级标题
st.subheader('This is a subheader')

# 展示代码，有高亮效果
code = '''def hello():
  print("Hello, Streamlit!")'''
st.code(code, language='python')

# 纯文本
st.text('This is some text.')

# LaTeX 公式
st.latex(r'''
  a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
  \sum_{k=0}^{n-1} ar^k =
  a \left(\frac{1-r^{n}}{1-r}\right)
''')