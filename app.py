import streamlit as st
def main():
    st.header("Hello, Streamlit!")
    name=st.text_input("Enter some text:")
    col1,col2=st.columns(2,gap='small')
    with col1:
    
        if st.button("Submit", type="primary",key='btn1',width='stretch' ):
            print('hi',name)

    with col2:
        if st.button('display',type='secondary',key='btn2'):
            print('bye',name)

    st.markdown("""
      <style>
                button{
                
                background-color: #4CAF50!important;
                }
                </style>
     
  """,unsafe_allow_html=True)#by this we can write all the html and css properties
    
main()