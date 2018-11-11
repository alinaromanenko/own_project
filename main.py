while True:
    file_str = input('Введите название файла: ')
    try:
        input_file = open (file_str,'r')
        break
    except FileNotFoundError:
        print('Файл {} не найден.'.format(file_str))
value = input('Введите слово, которое нужно исключить:')
with open ('output.txt', 'w') as output_file:
    for line in input_file:
        f_letter = int(line.find(value))
        l_letter = f_letter+len(value)
        print(line[:f_letter]+line[l_letter:], file= output_file, end='')