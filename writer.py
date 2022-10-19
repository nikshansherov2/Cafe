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