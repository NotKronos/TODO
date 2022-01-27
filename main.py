import os

opened_title: str = " "
opened_completed: int = 0
opened_elements: int = 0
opened_content: list


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def version():
    f = open(".version", "r")
    try:
        todo_version: str = f.read()
        print(f"TODO Version: {todo_version}")
    except OSError:
        print('Cannot open: ', f)
    except BaseException as err:
        print(f"Unexpected {err}, {type(err)}")
        raise
    f.close()


def todo_print(title: str, completed: int, elements: int, content: list):
    print(f"TODO {title}, [{completed}/{elements}]")
    counter: int = 0
    for line in content:
        counter += 1
        print(f"{counter}. {line} \n")


def todo_left(title: str, completed: int, elements: int, content: list):
    print(f"Left TODO {title}, [{completed}/{elements}]")
    counter: int = 0
    for line in content:
        if line.endswith(" DONE" + "\n"):
            counter += 1
            print(f"{counter}. {line} \n")
        else:
            pass


def todo_create():
    title: str = input("Podaj nazwę listy: ")
    try:
        open(title, "x")
        print(f"Utworzono plik listy {title}")
    except BaseException as err:
        print(f"Unexpected {err}, {type(err)}")
        raise


def todo_open():
    title: str = input("Jaką listę chcesz otworzyć: ")
    f = open(title, "r")
    try:
        global opened_title
        opened_title = title
        lines = f.readlines()
        global opened_content
        opened_content = lines
        for count, line in enumerate(lines):
            global opened_elements
            opened_elements = count
            if line.endswith(" DONE" + "\n"):
                global opened_completed
                opened_completed = 0
                opened_completed += 1
    except OSError:
        print('cannot open', f)
    f.close()


def todo_load(title: str):
    f = open(title, "r")
    try:
        global opened_title
        opened_title = title
        lines = f.readlines()
        global opened_content
        opened_content = lines
        for count, line in enumerate(lines):
            global opened_elements
            opened_elements = count
            if line.endswith(" DONE" + "\n"):
                global opened_completed
                opened_completed = 0
                opened_completed += 1
    except OSError:
        print('cannot open', f)
    f.close()


def todo_edit(title: str):
    f = open(title, "a")
    try:
        new_elements = int(input("Ile elementów chcesz dodać do listy: "))
        if os.path.getsize(title) == 0:
            f.write(input("Dodaj element listy: "))
            for element in range(new_elements - 1):
                element = input("Dodaj element listy: ")
                f.write(f"\n {element}")
        else:
            for element in range(new_elements):
                element = input("Dodaj element listy: ")
                f.write(f"\n {element}")
    except OSError:
        print('Cannot open: ', f)
    except BaseException as err:
        print(f"Unexpected {err}, {type(err)}")
        raise


def todo_set_as_done(title: str):
    f = open(title, "r")
    lines = f.readlines()
    for count, line in enumerate(lines):
        print(f"{count}. {line} \n")
    line_index = int(input("Który punkt chcesz oznaczyć jako wykonany: "))
    new_line = lines[line_index].rstrip("\n") + " DONE" + "\n"
    lines[line_index] = new_line
    f = open(title, "w")
    f.writelines(lines)
    f.close()


def menu():
    print("1: otwórz listę")
    print("2: wypisz zawartość listy")
    print("3: wyświetl nieukończone punkty listy")
    print("4: edytuj listę")
    print("5: oznacz punkt listy jako ukończony")
    print("6: utwórz nową listę")
    print("v: wyświetl wersję programu")
    print("e: opuść program")
    selection = input("Wybierz opcję: ")
    match selection:
        case '1':
            todo_open()
        case '2':
            todo_load(opened_title)
            todo_print(opened_title, opened_completed, opened_elements, opened_content)
        case '3':
            todo_load(opened_title)
            todo_left(opened_title, opened_completed, opened_elements, opened_content)
        case '4':
            todo_load(opened_title)
            todo_edit(opened_title)
        case '5':
            todo_load(opened_title)
            todo_set_as_done(opened_title)
        case '6':
            todo_create()
        case 'e':
            exit()
        case 'v':
            version()
        case _:
            print("Nieprawidłowa opcja")
    input("Naciśnij dowolny przycisk aby kontynuować...")
    clear_console()


while True:
    if opened_title == " ":
        print("1: stwórz listę")
        print("2: otwórz listę")
        option = input("Wybierz opcję: ")
        match option:
            case '1':
                todo_create()
            case '2':
                todo_open()
            case _:
                pass
    else:
        print(f"Obecnie otwarty plik: {opened_title}")
        menu()
