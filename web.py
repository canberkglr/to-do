import streamlit as st
import functions

st.title("My Todo App")
st.subheader("This is a todo app")
st.write("This app to increase your productivity.")

listem = functions.g_todos()
for ind, test in enumerate(listem):
    st.checkbox(test, key = ind)

st.text_input(label="", placeholder="Add new Todo")