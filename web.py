import streamlit as st
import functions

listem = functions.g_todos()

def add_todo():
    todo = st.session_state["new_todos"]
    listem.append(todo + "\n")
    functions.w_todos(listem)


st.title("My Todo App")
st.subheader("This is a todo app")
st.write("This app to increase your productivity.")


for ind, test in enumerate(listem):
    st.checkbox(test, key = ind)

st.text_input(label="", placeholder="Add new Todo", on_change=add_todo, key='new_todos')
