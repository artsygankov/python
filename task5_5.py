# Program to create text file with random numbers separated by space
from random import random

file_name = 'text3.txt'
numbers_count = 10
numbers_list = []
out_line = ''
usr_sum = 0
with open(file_name, 'w') as out_file:
    for idx in range(1, numbers_count + 1):
        out_line += str(round(random() * 100)) + ' '
    out_file.write(out_line)
with open(file_name, 'r') as in_file:
    for line in in_file:
        numbers_list = line.split()
for num in numbers_list:
    usr_sum += int(num)
print(usr_sum)
