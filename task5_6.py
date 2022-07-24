# Program to parse timetable
file_name = 'timetable.txt'
result_dict = {}
subjects_type_list = ('(л)', '(пр)', '(лаб)', '-', '\n')
sum_list = []
part1 = part2 = ''
with open(file_name, 'r', encoding="utf-8") as in_file:
    for out_line in in_file:
        sum_academic_hours = 0
        part1, part2 = out_line.split(':')
        for subj in subjects_type_list:
            part2 = part2.replace(subj, '|0|')
        sum_list = part2.split('|')
        for idx in sum_list:
            if idx == '':
                idx = 0
            sum_academic_hours += int(idx)
        result_dict[part1] = sum_academic_hours
print(result_dict)
