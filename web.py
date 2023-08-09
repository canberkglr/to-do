import streamlit as st
import functions

listem = functions.g_todos()

def add_todo():
    todo = st.session_state["new_todos"]
    st.session_state["new_todo"] = ""
    listem.append(todo + "\n")
    functions.w_todos(listem)


st.title("My Todo App")
st.subheader("This is a todo app")
st.write("This app to increase your productivity.")


for id, test in enumerate(listem):
    st.checkbox(test, key = id)
    if st.session_state[id]:
        listem.pop(id)
        functions.w_todos(listem)
        del st.session_state[id]
        st.experimental_rerun()


st.text_input(label="", placeholder="Add new Todo", on_change=add_todo, key='new_todos')
