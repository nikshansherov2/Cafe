def show_staff():
    path = 'dates/staff.csv'
    data = open(path, 'r', encoding='utf-8')
    for line in data:
        print(line.strip())
    data.close()


def show_table():
    path = 'dates/tables.csv'
    data = open(path, 'r', encoding='utf-8')
    for line in data:
        print(line.strip())
    data.close()


def show_tables_of_empl(id_empl):
    with open('dates/staff.csv', encoding='utf-8') as s, open('dates/match.csv', encoding='utf-8') as m:
        name = ''
        for i in s:
            temp = i.split(';')
            if temp[0] == id_empl:
                name = temp[1]
        tables = ''
        for i in m:
            temp = i.strip().split(';')
            if temp[1] == id_empl:
                tables += temp[2]+' '
        print(f'{id_empl} {name}: {tables}')


def get_name(id_empl):
    with open('dates/staff.csv', encoding='utf-8') as s:
        for i in s:
            temp = i.strip().split(';')
            if temp[0] == id_empl:
                name = temp[1]
        return name


def get_number(id_table):
    with open('dates/tables.csv', encoding='utf-8') as s:
        for i in s:
            temp = i.strip().split(';')
            if temp[0] == id_table:
                name = temp[1]
        return name
