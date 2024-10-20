import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    to_do = st.session_state['new_todo'] + "\n"
    todos.append(to_do)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is a Todo-App. ")
st.write("This app is to run web pages.")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
