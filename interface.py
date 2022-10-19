import reader as r
import writer as w
import exceptions as e
import deals as d
import logger as l


def for_empls():
    print("Введите 1 для добавления сотрудника\nВведите 2 для удаления сотрудника\n\
    Введите 'q' для выхода\nВведите 'r' для возврата в предыдущее меню")
    choice = input("Ввод: ")
    print()
    if choice == '1':
        name = input("Введите имя нового сотрудника в виде 'О.С.Сидоров': ")
        post = input("Введите должность нового сотрудника: ")
        entity = name, post
        w.add_empl(entity)
        l.log(f"Добавлен сотрудник {name}")
        exit()
    elif choice == '2':
        r.show_staff()
        id_empl = input("Введите ID сотрудника: ")
        if e.check_id_empl(id_empl):
            w.del_empl(id_empl)
            l.log(f"Удален сотрудник {r.get_name(id_empl)} с ID {id_empl}")
            exit()
        else:
            print("Такого сотрудника нет\n")
    elif choice == 'q':
        exit()
    elif choice == 'r':
        return
    else:
        print("Некорректный ввод\n")


def for_tables():
    while True:
        print("Введите 1 для добавления столика\nВведите 2 для удаления столика\n\
        Введите 'q' для выхода\nВведите 'r' для возврата в предыдущее меню")
        choice = input("Ввод: ")
        print()
        if choice == '1':
            num = input("Введите номер нового столика: ")
            if not e.check_table(num):
                w.add_table(num)
                l.log(f"Добавлен столик с номером {num}")
                exit()
            else:
                print("Такой столик уже есть\n")
        elif choice == '2':
            r.show_table()
            id_table = input("Введите ID столика: ")
            if e.check_id_table(id_table):
                w.del_table(id_table)
                l.log(f"Удален столик {r.get_number(id_table)} с ID {id_table}")
                exit()
            else:
                print("Такого столика нет\n")
        elif choice == 'q':
            exit()
        elif choice == 'r':
            return
        else:
            print("Некорректный ввод\n")


def for_staff():
    while True:
        print(f"Введите 1 для работы со списком сотрудников\nВведите 2 для работы со списком столиков\n\
        Введите 'q' для выхода\nВведите 'r' для возврата в предыдущее меню")
        choice = input("Ввод: ")
        print()
        if choice == '1':
            for_empls()
        elif choice == '2':
            for_tables()
        elif choice == 'q':
            exit()
        elif choice == 'r':
            return
        else:
            print("Некорректный ввод\n")


def for_deals():
    while True:
        r.show_staff()
        id_empl = input("Введите ID сотрудника заключившего сделку: ")
        r.show_table()
        id_table = input("Введите ID обслуженного сотрудником столика: ")
        if e.check_match(id_empl, id_table):
            d.add_deal(id_empl, id_table)
            l.log(f"Сотрудник {r.get_name(id_empl)} с ID {id_empl} обслужил\
             столик номер {r.get_number(id_table)} с ID {id_table}")
            return
        else:
            if e.check_id_empl(id_empl):
                r.show_tables_of_empl(id_empl)
                print("Этот сотрудник не обслуживает этот столик\n")
            else:
                print("Некорректный ввод\n")


def work_mode():
    while True:
        print("Введите 1 для работы с персоналом\nВведите 2 для заключения сделки\n\
        Введите 'q' для выхода")
        choice = input("Ввод: ")
        print()
        if choice == '1':
            for_staff()
        elif choice == '2':
            for_deals()
        elif choice == 'q':
            exit()
        else:
            print("Некорректный ввод\n")
