import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home

def home_screen():
    
    header_home()
    style_background_home()
    style_base_layout()
    col1, col2 = st.columns(2)

    with col1:
        st.header("I am Teacher")
        st.image("https://img.magnific.com/premium-vector/vector-logo-illustration-teacher-mascot-cartoon-style_116762-8535.jpg?semt=ais_hybrid&w=740&q=80", width=145)
        if st.button("teacher portal", type="primary"):
            st.session_state["login_type"] = "teacher"
            st.rerun()

    with col2:
        st.header("I am Student")
        st.image("https://d1csarkz8obe9u.cloudfront.net/posterpreviews/logo-design-template-35b0a3e2315d19a46c046165f315b000.jpg?ts=1592240511", width=145)
        if st.button("student portal", type="primary"):
            st.session_state["login_type"] = "student"
            st.rerun()
            
            
    footer_home()    