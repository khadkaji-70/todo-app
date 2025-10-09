import streamlit as st
from functions import get_todos, write_todos

st.title("✅ To-Do App")

todos = get_todos()

def add_todo():
    todo = st.session_state["newTodo"].strip()
    if todo:
        todos.append(todo + "\n")
        write_todos(todos)
        st.session_state["newTodo"] = ""

for i, todo in enumerate(todos):
    checkbox_state = st.checkbox(todo.strip(), key=f"todo_{i}")
    if checkbox_state:

        todos.pop(i)
        write_todos(todos)

        # Delete its checkbox key so it doesn't stay checked
        del st.session_state[f"todo_{i}"]
        st.rerun()

st.text_input(
    label="To-Do Item",
    placeholder="Enter a to-do",
    on_change=add_todo,
    key="newTodo",
    label_visibility="collapsed"
)
