import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background-color: #5865f2 !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background-color: #E0E3FF !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
                
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Outfit:wght@100..900&family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');
        
        
        
            /*hide toolbar of streamlit*/
            #mainmenu, footer, header {
                visibility: hidden;
                }
            .block-container{
                padding-top: 1.5rem;
            }
            
            h1{
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
                
            }
            
            
                        h2{
                            font-family: 'Climate Crisis', sans-serif !important;
                            font-size: 3.5rem !important;
                            line-height: 1.1 !important;
                            margin-bottom: 0rem !important;
                        }
                        
                        
                        h3,h4,p{
                            
                            font-family: 'outfit', sans-serif;
                        }
                        
                        
                                                button{
                                                    background:#5865F2 !important;
                                                    border-radius: 1.5rem !important;
                                                    color: white !important;
                                                    padding: 10px 20px !important;
                                                    border: none !important;
                                                    transition: transform 0.25s ease-in-out !important;
                                                }
                                                
                                                
                                                
                                                
                                                                        button[kind="tertiary"]{
                                                                            background:black !important;
                                                                            border-radius: 1.5rem !important;
                                                                            color: white !important;
                                                                            padding: 10px 20px !important;
                                                                            border: none !important;
                                                                            transition: transform 0.25s ease-in-out !important;
                                                                        }
                        
                        button[kind="secondary"]{
                            background:#EB459E !important;
                            border-radius: 1.5rem !important;
                            color: white !important;
                            padding: 10px 20px !important;
                            border: none !important;
                            transition: transform 0.25s ease-in-out !important;
                        }
                        
                        button:hover{
                            transform: scale(1.05) !important;
                        }
        </style>
    """, unsafe_allow_html=True)
    
    
#video number 1026 18.51 sec date 1/9/2026