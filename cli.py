import time
import functions

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()
    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action.split(' ', 1)[1]
        todos = functions.get_todos()
        todos.append(todo.title()+'\n')
        functions.write_todos(todos)
    elif user_action.startswith('show'):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = f"{index + 1}-{item}"
            print(item)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action.split(' ', 1)[1]) - 1

            todos = functions.get_todos()

            existing_todo = todos[number]
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo.title() + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

        except IndexError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action.split(' ', 1)[1]) - 1

            todos = functions.get_todos()

            ex_todo = todos.pop(number)
            ex_todo = ex_todo.strip('\n')

            functions.write_todos(todos)

            message = f"Todo '{ex_todo}' was removed from the todos list"
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Hey, you entered an unknown command")

print("The END!")
