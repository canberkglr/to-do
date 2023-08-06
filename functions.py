

def g_todos(filename="todos.txt"):
    """
    Read lines from txt
    """

    with open(filename, "r") as file:
        todos_l = file.readlines()
    return todos_l


def w_todos(todos_l, filename="todos.txt"):
    """
    Write files to txt
    """
    with open(filename, "w") as file:
        file.writelines(todos_l)
