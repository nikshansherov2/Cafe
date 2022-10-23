import csv


def check_id_empl(id_empl):
    with open('dates/staff.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            print(row[0])
            if row[0] == id_empl:
                return True
            else:
                continue
    return False


def check_table(num_table):
    with open('dates/tables.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if row[1] == num_table:
                return True
            else:
                continue
    return False


def check_id_table(id_table):
    with open('dates/tables.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if row[0] == id_table:
                return True
            else:
                continue
    return False


def check_match(id_empl, id_table):
    with open('dates/match.csv', 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            # print(row[1], row[2])
            if row[1] == id_empl and row[2] == id_table:
                return True
            else:
                continue
    return False
