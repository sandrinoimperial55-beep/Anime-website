import streamlit as st
import requests

st.header("GET IN TOUCH WITH ME")

with st.container():
    st.markdown(f"""
    <form action="https://formsubmit.co/sandrinoimperial55@gmail.com" method="POST">
       <input type="text" name="name" placeholder="your name" required style="width:100%; padding:10px; margin-bottom:10px;">
       <input type="email" name="email" placeholder="your email" required style="width:100%; padding:10px; margin-bottom:10px;">
       <textarea name="message" placeholder="your message" required style="width:100%; padding:10px; margin-bottom:10px;"></textarea>
       <input type="hidden" name="_captcha" value="false">
       <input type="hidden" name="_template" value="table">
       <button type="submit" style="width:100%; padding:10px; background-color:#ff4b4b; color:white; border:none; border-radius:5px;">Send</button>
   </form>""",unsafe_allow_html=True
   )
