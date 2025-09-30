from functions import *
import FreeSimpleGUI as sg

label=sg.Text("Type in a to-do")
inputBox=sg.Input(tooltip="Enter a to-do",key="todo")
addButton=sg.Button("Add")


window=sg.Window('My To-Do App',
                 layout=[[label],[inputBox,addButton],],
                 font=("Helvetica",12)
                 )
while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos=get_todos()
            new_todo=values['todo']+"\n"
            todos.append(new_todo)
            write_todos(todos)
        case sg.WINDOW_CLOSED:
            break




window.close()

