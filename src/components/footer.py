import streamlit as st

def footer_home():
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: center; margin-top: 20px;">
            <p style="text-align: center; color: white; font-weight: bold;">
                Made by 
                <a href="https://portfolio-ayush-azure.vercel.app" 
                   target="_blank"
                   style="color: white; ">
                    Ayush Saxena
                </a>
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    

def footer_dashboard():
    st.markdown("""
        <div style="display: flex; align-items: center; justify-content: center; margin-top: 20px;">
            <p style="text-align: center; color: white; font-weight: bold;">
                Made by 
                <a href="https://portfolio-ayush-azure.vercel.app" 
                   target="_blank"
                   style="color: black; ">
                    Ayush Saxena
                </a>
            </p>
        </div>
    """, unsafe_allow_html=True)