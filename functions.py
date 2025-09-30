def get_todos(filepath="todolist.txt"):
    with open(filepath) as f:
        lines = f.readlines()
        return lines

def write_todos(lines, filepath="todolist.txt"):
    with open(filepath, "w") as f:
        f.writelines(lines)

if __name__=="__main__":
    print("Hello")
    print(get_todos())
