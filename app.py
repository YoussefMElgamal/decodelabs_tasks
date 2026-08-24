import streamlit as st
from Decode_labs_chatbot import get_response

st.set_page_config(page_title="DecodeBot", page_icon="🤖")
st.title("🤖 DecodeBot")
st.caption("Week 1 Project — Rule-Based Chatbot (DecodeLabs AI Internship)")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! Type something like 'hello', 'help', or 'bye'."}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    response = get_response(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)