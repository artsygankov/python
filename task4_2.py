# Program to generate new list every
# Was copied from Eugeniy's decision
first_list = [12, 55, 84, 29, 31, 92, 29, 25, 62]
result_list = [first_list[count_list] for count_list in range(1, len(first_list)) if
               first_list[count_list] > first_list[count_list - 1]]
print(result_list)
