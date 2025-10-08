from functions import *
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
inputBox = sg.Input(tooltip="Enter a to-do", key="todo")
addButton = sg.Button("Add")
listBox = sg.Listbox(values=get_todos(), key='todos', enable_events=True, size=(45, 12))
editButton = sg.Button("Edit")
completeButton = sg.Button("Complete")
exitButton = sg.Button("Exit")
layout=[[label], [inputBox, addButton], [listBox, editButton,completeButton],[exitButton]]
window = sg.Window('My To-Do App',
                   layout=layout,
                   font=("Helvetica", 12)
                   )
while True:
    event, values = window.read()
    print(event, values)

    match event:
        case 'Add':
            todos = get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            todoToEdit=values['todos'][0]
            new_todo = values['todo']
            todos=get_todos()
            index=todos.index(todoToEdit)
            todos[index]=new_todo+"\n"
            write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case "Complete":
            todoToComplete=values['todos'][0]
            todos=get_todos()
            todos.remove(todoToComplete)
            write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")

        case "Exit":
            window.close()
            break

        case sg.WINDOW_CLOSED:
            break

window.close()
