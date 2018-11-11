border = 0
while True:
    file_str = input('Введите название файла: ')
    try:
        input_file = open (file_str,'r')
        break
    except FileNotFoundError:
        print('Файл {} не найден.'.format(file_str))
value = input('Введите то, что нужно исключить: ')

# Чтобы удалить слово, необходимо ввести его с 1 пробелом в начале или в конце.

with open('output.txt', 'w') as output_file:
    for line in input_file:
        for i in range(len(line)):
            if border != len(line):
                f_letter = int(line.find(value, border))
                if f_letter != border:
                    print(line[border], file=output_file, end='')
                    border = border + 1
                else:
                    border = border + len(value)
            else:
                break
if f_letter == -1:
    print('В файле {} "{}" не найдено.'.format(file_str, value))
