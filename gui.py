import functions
import PySimpleGUI as gui
import time

gui.theme("Black")

clock = gui.Text('', key="Clock")
label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter a todo", key="todo")
add_button = gui.Button("Add")
list_box = gui.Listbox(values=functions.get_todos(),
                       key='todos', enable_events=True,
                       size=(45, 10))
edit_button = gui.Button("Edit")
complete_button = gui.Button("Complete")
exit_button = gui.Button("Exit")

layout = [[clock],
          [label],
          [input_box, add_button],
          [list_box, edit_button, complete_button],
          [exit_button]]
window = gui.Window("My To-Do App",
                    layout=layout,
                    font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print("event", event)
    print("values", values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                gui.popup("Please select an item first!", title="ERROR!", font=("Helvetica", 20))

        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update('')
            except IndexError:
                gui.popup("Please select an item first!", title="ERROR!", font=("Helvetica", 20))

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case "Exit":
            break

        case gui.WINDOW_CLOSED:
            break

        case _:
            continue
print('Bye')
window.close()
