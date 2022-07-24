# Program to change numeric
in_file_name = 'text1.txt'
out_file_name = 'text2.txt'
numeric_basis = ('One', 'Two', 'Three', 'Four')
numeric_change = ('Один', 'Два', 'Три', 'Четыре')
with open(in_file_name, 'r') as in_file:
    with open(out_file_name, 'w') as out_file:
        for line in in_file:
            for idx in range(0, len(numeric_basis)):
                if line.find(numeric_basis[idx]) != -1:
                    out_file.write(line.replace(numeric_basis[idx], numeric_change[idx]))
