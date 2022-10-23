import interface as i


print('Для работы в консоли введите - 1\nДля работы в графической оболочке введите - 2')
n = input('Ввод: ')
if n == '1':
    i.work_mode()
elif n == '2':
    import gui
else:
    print('Неправильный выбор!')
