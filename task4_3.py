# Program to find numbers which could be devided by 20 and 21
result_list = [probe_number for probe_number in range(20, 241) if (probe_number % 20 == 0) or (probe_number % 21 == 0)]
print(result_list)
