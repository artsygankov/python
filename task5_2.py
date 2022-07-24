# Program to calculate lines and words in each line in some text file

file_name = 'users_text_file.txt'
with open(file_name, 'r') as opened_file:
    file_line = 'a'
    file_str = 0
    file_words = 0
    file_line = []
    while file_line != '':
        file_line = opened_file.readline()
        file_str += 1
        print(f' Всего слов в строке {file_str} - {len(file_line.split())}')
print(f'Всего в файле {file_str} строк')
