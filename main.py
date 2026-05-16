import streamlit as st 
from services.auth.login_wall import render_login_wall

def main():
    st.set_page_config(page_title="Ai real-time Workout Coach", 
                       page_icon="🏋️‍♂️", 
                       layout="centered",
                       initial_sidebar_state="expanded")
    if not render_login_wall():
        return
if __name__ == "__main__":
    main()

