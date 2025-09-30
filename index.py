#enumerate creates an object with structure:[(index,item),(index,item)]. This kind of object makes it possible to iterate using two variable
from functions import *
import time

now=time.strftime("%m/%d/%Y %I:%M:%S %p")
print(f"Today is {now}")
while True:
  user_action=input("Enter add, show, edit, complete or exit: ")
  user_action=user_action.strip() 


  if  user_action.startswith("add"):
    todo=user_action[4:] #slicing of list after index 4
    # todo=input("Enter a todo: ")+"\n"
    todos= get_todos()

    todos.append(todo + '\n')
    print(f" {todo.strip('\n')}  was added")

    write_todos(todos)

  elif  user_action.startswith("show"):
    todos= get_todos()

    # new_todos=[]
    # for item in todos:
    #   new_item=item.strip("\n")
    #   new_todos.append(new_item)\

    new_todos= [item.strip("\n") for item in todos]
    print("Your Todo are: ")
    for number,item in enumerate(new_todos):
      # item=item.strip("\n")
      print(f"{number+1}.{item}")

  elif user_action.startswith("edit"):
    try:
      todos= get_todos()

      number=user_action[5:]
      previous_todo=todos[int(number)-1]
      edited_todo=input("Enter Todo: ")
      todos[int(number)-1]=edited_todo + '\n'
      print(f"Successfully edited {previous_todo.strip("\n")} to {edited_todo}")

      write_todos(todos)
    except ValueError:
      print("Sorry, you didn't enter a valid number")
      continue



  elif user_action.startswith("complete"):
    try:
      todos= get_todos("todolist.txt")
      number=int(user_action[8:])
      index=number-1
      todo_to_remove=todos[index]
      todos.pop(index)
      print(f"{todo_to_remove.strip('\n')} was removed")

      write_todos(todos)
    except IndexError:
      print("Sorry, you didn't enter a valid number")
      continue

  elif user_action.startswith("exit"):
    print("Thank you!!")
    break
  else:
    print("Not valid")




