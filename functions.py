
FILE_PATH="todos.txt"
def g_todos(filename=FILE_PATH):
    """
    Read lines from txt
    """

    with open(filename, "r") as file:
        todos_l = file.readlines()
    return todos_l


def w_todos(todos_l, filename=FILE_PATH):
    """
    Write files to txt
    """
    with open(filename, "w") as file:
        file.writelines(todos_l)
