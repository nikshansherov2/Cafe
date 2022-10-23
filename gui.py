from tkinter import *
import tkinter.messagebox as mb
import reader as r
import writer as w
import exceptions as e
import deals as d
import logger as l

def add_staff(ent_1, ent_2):
    entity = ent_1.get(), ent_2.get()
    w.add_empl(entity)
    l.log(f"Добавлен сотрудник {ent_1.get()}")

def del_staff(ent):
    if e.check_id_empl(ent.get()):
        w.del_empl(ent.get())
        l.log(f"Удален сотрудник {r.get_name(ent.get())} с ID {ent.get()}")
    else:
        mb.showerror('Ошибка', 'Такого сотрудника не существует!')
        ent.delete(0, END)

def add_table(ent):
    num = ent.get()
    if not e.check_table(num):
        w.add_table(num)
        l.log(f"Добавлен столик с номером {num}")
    else:
        pass

def del_table(ent):
    if e.check_id_table(ent.get()):
        w.del_table(ent.get())
        l.log(f"Удален столик {r.get_number(ent.get())} с ID {ent.get()}")
    else:
        mb.showerror('Ошибка', 'Такого столика не существует!')
        ent.delete(0, END)

def add_deals(ent_1, ent_2):
    if e.check_match(ent_1.get(), ent_2.get()):
        d.add_deal(ent_1.get(), ent_2.get())
        l.log(f"Сотрудник {r.get_name(ent_1.get())} с ID {ent_1.get()} обслужил\
             столик номер {r.get_number(ent_2.get())} с ID {ent_2.get()}")
    else:
        r.show_tables_of_empl(ent_1)
        mb.showerror('Ошибка', 'Данный сотрудник не обслуживает этот столик')
        ent_1.delete(0, END)
        ent_2.delete(0, END)

def window_add_staff():
    new_wind = Toplevel(root)
    new_wind.geometry('400x150+650+350')
    new_wind.title('Добавление сотрудника')
    lab_1 = Label(new_wind, width=50, text='Введите имя сотрудника в формате И.В. Петров')
    lab_2 = Label(new_wind, width=50, text='Введите должность сотрудника')
    ent_1 = Entry(new_wind, width=30)
    ent_2 = Entry(new_wind, width=30)
    but = Button(new_wind, text='Добавить', command=lambda: add_staff(ent_1, ent_2))
    lab_1.pack()
    ent_1.pack()
    lab_2.pack()
    ent_2.pack()
    but.pack()


def window_delete_staff():
    new_wind = Toplevel(root)
    new_wind.geometry('300x100+650+350')
    new_wind.title('Удаление сотрудника')
    lab = Label(new_wind, width=50, text='Введите ID сотрудника')
    ent = Entry(new_wind, width=10)
    but = Button(new_wind, text='Ввести', command=lambda: del_staff(ent))
    lab.pack()
    ent.pack()
    but.pack()

def window_add_table():
    new_wind = Toplevel(root)
    new_wind.geometry('300x100+650+350')
    new_wind.title('Добавление столика')
    lab = Label(new_wind, width=30, text='Введите номер нового столика')
    ent = Entry(new_wind, width=10)
    but = Button(new_wind, text='Добавить', command=lambda: add_table(ent))
    lab.pack()
    ent.pack()
    but.pack()

def window_delete_table():
    new_wind = Toplevel(root)
    new_wind.geometry('300x100+650+350')
    new_wind.title('Удаление столика')
    lab = Label(new_wind, width=50, text='Введите ID столика')
    ent = Entry(new_wind, width=10)
    but = Button(new_wind, text='Ввести', command=lambda: del_table(ent))
    lab.pack()
    ent.pack()
    but.pack()

def window_add_deals():
    new_wind = Toplevel(root)
    new_wind.geometry('400x150+650+350')
    new_wind.title('Добавление сделки')
    lab_1 = Label(new_wind, width=50, text='Введите ID сотрудника')
    lab_2 = Label(new_wind, width=50, text='Введите ID столика')
    ent_1 = Entry(new_wind, width=10)
    ent_2 = Entry(new_wind, width=10)
    but = Button(new_wind, text='Добавить', command=lambda: add_deals(ent_1, ent_2))
    lab_1.pack()
    ent_1.pack()
    lab_2.pack()
    ent_2.pack()
    but.pack()

root = Tk()
root.geometry('900x600+500+200')
root.title('Кафе Питон')
img = PhotoImage(file="img/cafe.gif")
Label(root, image=img).pack()
mainmenu = Menu(root)
root.config(menu=mainmenu)
staffmenu = Menu(mainmenu, tearoff=0)
staffmenu.add_command(label='Добавить сотрудника', command=window_add_staff)
staffmenu.add_command(label='Удалить сотрудника', command=window_delete_staff)
tablesmenu = Menu(mainmenu, tearoff=0)
tablesmenu.add_command(label='Добавить столик', command=window_add_table)
tablesmenu.add_command(label='Удалить столик', command=window_delete_table)
dealsmenu = Menu(mainmenu, tearoff=0)
dealsmenu.add_command(label='Добавить сделку', command=window_add_deals)
mainmenu.add_cascade(label='Персонал', menu=staffmenu)
mainmenu.add_cascade(label='Столики', menu=tablesmenu)
mainmenu.add_cascade(label='Сделка', menu=dealsmenu)
root.mainloop()
