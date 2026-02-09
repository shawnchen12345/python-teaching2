import streamlit as st
st.title('问候器')
name= st.text_input("请输入你的名字")
role=st.selectbox("选择你喜欢的角色", ['劳达',"出身", "学神", "劳氏"])
if role==('出身'):
    st.write('fuck off')
elif role==('劳氏'):
    st.button('welcome')
    st.balloons()
elif role==('劳达'):
    st.snow()
st.write(f"你好，{name}！ 👋 欢迎来到系统。您当前的身份是 {role}。")
col1,col2=st.columns(2)
with col1:
    st.image('https://p1.ssl.qhimgs1.com/sdr/400__/t045fa82cdc30ed428b.jpg',caption='劳达')
    if st.button('吃劳达肘击'):
        st.markdown('<span style='font-size:50px;'>man!!!!</span>',unsafe_allow_html=true)
with col2:
    st.image('https://p3.ssl.qhimgs1.com/sdr/400__/t013c0b1d6619932ef9.jpg',caption='helicopter')
    if st.button('孩子们我能活下来吗？'):
        st.balloons()







