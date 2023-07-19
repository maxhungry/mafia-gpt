from contextlib import contextmanager

import streamlit as st


class ChatDisplay:
    def __init__(self, name, avatar=None) -> None:
        self.name = name
        self.avatar = avatar

    def show(self, message):
        with st.chat_message(self.name, avatar=self.avatar):
            st.write(f"{self.name}: {message}")

    @contextmanager
    def stream(self):
        with st.chat_message(self.name, avatar=self.avatar):
            st.write(f"{self.name}: ")
            message_placeholder = st.empty()
            yield message_placeholder
