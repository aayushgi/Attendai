import streamlit as st

from src.ui.base_layout import (
    style_background_home,
    style_base_dashboard,
    style_base_layout
)

from src.components.header import header_dashboard


def teacher_screen():

    # Apply dashboard background
    style_base_dashboard()

    # Apply common styling
    style_base_layout()

    # Display header
    c1,c2=st.columns(2, vertical_alignment="center",gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        st.button("go back to home",type="secondary",key='loginbackbtn',shortcut="Ctrl+Backspace")
    # Page title
    st.title("Teacher Screen")


    # Add more functionality for the teacher screen here