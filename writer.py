# add_empl() – принимает кортеж из 2-ух элементов (строки): 1-ый – имя сотрудника (О.С.Пупкин), 2-ой – должность (Официант). Ничего не возвращает. Добавляет в файл staff.csv нового сотрудника, его должность и присваивает ему новое ID (для этого нужно проверить какие ID уже есть и взять следующее число, можно просто найти максимальное и сделать +1).
# 
#  Если добавить нового сотрудника, то нужно перераспределить столики в файле match.csv. Количество столиков дели с остатком на сотрудников, а остальным по порядку по одному добавь. Можешь перераспределение столиков вынести в отдельную функцию (это на твое усмотрение).


# del_empl() – принимает строку из числа (ID). Проверку делать не надо. Ничего не возвращает. Удаляешь сотрудника с этим ID из staff.csv. И делаешь пересчет столиков между оставшимися сотрудниками файле match.csv.
# add_table() - принимает строку из числа (номер столика, не ID). Проверку делать не надо. Ничего не возвращает. Добавляет в файл table.csv номер столика и присваивает ему уникальный ID. Делаешь перерасчет столиков между сотрудниками файле match.csv.
# del_table() - принимает строку из числа (ID). Проверку делать не надо. Ничего не возвращает. Удаляешь столик с этим ID из table.csv. И делаешь пересчет оставшихся столиков между сотрудниками файле match.csv.

import os

defaultStaff='dates/staff.csv'
defaultMatch='dates/match.csv'
defaultTables='dates/tables.csv'

def add_empl(tpl):
    id=str(getFreeId(defaultStaff))
    with open(defaultStaff,'a',encoding='utf-8') as staff:
        staff.write('\n'+id+';'+tpl[0]+';'+tpl[1])
    reMatch(defaultTables,defaultStaff,defaultMatch)

def del_empl(id_empl):
    delFromFile(defaultStaff,id_empl)
    reMatch(defaultTables,defaultStaff,defaultMatch)

def add_table(num):
    id=str(getFreeId(defaultTables))
    with open(defaultTables,'a',encoding='utf-8') as tables:
        tables.write('\n'+id+';'+num)
    reMatch(defaultTables,defaultStaff,defaultMatch)

def del_table(id_table):
    delFromFile(defaultTables,id_table)
    reMatch(defaultTables,defaultStaff,defaultMatch)

def getFreeId(path):
    with open(path,'r',encoding='utf-8') as staff:
        ids=[]
        for line in staff:
            person=(line.strip('\n').split(';'))
            if not person[0].isdigit():
                continue
            ids.append(int(person[0]))
            ids.sort()
    if ids[0]!=1:
        return 1
    for i in range(1,len(ids)):
        if (ids[i]-1)!=ids[i-1]:
            return (ids[i])-1
    return max(ids)+1

def delFromFile(Path,id):
    with open(Path, 'r', encoding="utf-8") as file, \
        open('dates/data.tmp', "w", encoding="utf-8") as t:
        for line in file:
            ID=(line.split(';'))[0]
            fixed=line.strip('\n')
            if not id==ID:
                if ID.isdigit():
                    t.write('\n'+fixed)
                else:
                    t.write(fixed)
    with open('dates/data.tmp', "r", encoding="utf-8") as t, \
        open(Path, 'w', encoding="utf-8") as file:
        for line in t:
            file.write(line)
    os.remove('dates/data.tmp')

def reMatch(defaultTables,defaultStaff,defaultMatch):
    with open(defaultTables,'r',encoding='utf-8') as t:
        tables=[]
        for line in t:
            tables.append((line.strip('\n').split(';'))[0])
        tables.remove('ID')
    with open(defaultStaff,'r',encoding='utf-8') as staff:
        employees=-1
        for line in staff:
            if line != "\n":
                employees+=1
    sharedTables=[]
    count=1
    for table in range(len(tables)):
        count+=1
        if not table%employees:
            count=1
        sharedTables.append(count)
    with open(defaultMatch,'w',encoding='utf-8') as match:
        id=1
        for table in range(len(tables)):
                if table==0:
                    match.write('ID;id_empl;id_table')
                match.write(f'\n{id};{sorted(sharedTables)[table]};{tables[table]}')
                id+=1




# tpl=('О.С.Пупкин','Официант')
# id_empl='7'
# num='666'
# id_table='16'
# id='1'
# # add_empl(tpl)
# # del_empl(id_empl)
# # reMatch(defaultTables,defaultStaff,defaultMatch)
# # add_table(num)
# del_table(id_table)