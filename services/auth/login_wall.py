import streamlit as st 

def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True
    
    st.title("Ai real-time Workout Coach")
    st.markdown("### Welcome! Please Enter Your Usename ")

    with st.form("login_form", clear_on_submit=False):
        username - st.text_input("Username", placeholder="Unique name to identify you")
        submit_button = st.form_submit_button("Submit", width="stretch")
    
    if submit_button:
        if not username:
            st.error("Username cannot be empty.")
            return False
        st.session_state["user_id"] = username

    return False