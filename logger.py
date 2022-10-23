from datetime import datetime as dt

def log(line):
    today = dt.now().strftime('%d-%m-%Y %H:%M:%S ')
    with open ('log.txt', 'a') as file1:
        file1.write(f'{today} {line}\n')


