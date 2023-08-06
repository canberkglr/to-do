import functions
import time

a = time.strftime("%b %d, %Y %H:%M:%S")
print(a)

while True:
    action = input("Type add, show, edit, complete or exit: ")
    action = action.strip()

    if action.startswith("add"):
        todo = action[4:]
        todos = functions.g_todos()
        todos.append(todo + "\n")

        functions.w_todos(todos)

    elif action.startswith("edit"):
        try:
            todos = functions.g_todos()
            ind = int(action[5:])
            ind = ind - 1
            new = input("Print new item: ")
            todos[ind] = new + '\n'
            functions.w_todos(todos)
        except ValueError:
            print("Command is invalid")
        except IndexError:
            print("Index is out of range")

    elif action.startswith("show"):
        todos = functions.g_todos()

        todos = [item.strip() for item in todos]
        for index, item in enumerate(todos):
            item_index = todos.index(item) + 1
            fstr = f"{index + 1}-{item}"
            print(fstr)

    elif action.startswith("complete"):
        try:
            ind = int(action[9:])
            todos = functions.g_todos()
            todos.pop(ind - 1)
            functions.w_todos(todos)
        except ValueError:
            print("Command is invalid")
        except IndexError:
            print("Index is out of range")
    elif action.startswith("exit"):
        break
    else:
        print("Command in invalid.")
print("Bye!")
