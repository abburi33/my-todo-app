def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as todoFile:
        todos_local = todoFile.readlines()
    return todos_local


def write_todos(new_todos, filepath="todos.txt"):
    """ Write the to-do items list  in the text file."""
    with open(filepath, "w") as todoFile:
        todoFile.writelines(new_todos)