from datetime import datetime as dt

def add_deal(id_empl, id_table):
    today = dt.now().strftime('%d-%m-%Y %H:%M:%S ')
    with open ('done_deals.txt', 'a') as file1:
        file1.write(f'{today} Сотрудник ID:{id_empl} Столик ID:{id_table}\n')


