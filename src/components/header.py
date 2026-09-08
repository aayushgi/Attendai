import streamlit as st

def header_home():
    logo_url = "https://home.edweb.net/wp-content/uploads/snapchat.jpg"

    st.markdown(f"""
        <div style="display: flex; flex-direction:column; align-items: center; justify-content: center; margin-bottom: 20px; margin-top: 20px;">
            <img src="{logo_url}" style="height:100px;">
            <h1 style="text-align: center; color: white;">AttendAI</h1>
        </div>
    """, unsafe_allow_html=True)