# Program to work with jason
import json

file_name_txt = 'firms_list.txt'
file_name_json = 'firms_list.json'
firms_list = []
firms_dict = {}
avg_profit_dict = {}
out_line = ''
proxy_line = ''
firm_name = ''
firm_form = ''
gain = 0
expensis = 0
profit = 0
avg_profit = 0
count_1 = 0
with open(file_name_txt, 'r', encoding="utf-8") as in_file:
    for in_line in in_file:
        firm_name, firm_form, gain, expensis = in_line.split()
        profit = float(gain) - float(expensis)
        if profit > 0:
            count_1 += 1
            avg_profit = avg_profit + profit
        firms_dict[firm_name.replace('_', ' ')] = int(profit)
    avg_profit = avg_profit / count_1
    avg_profit_dict['average profit'] = avg_profit
    firms_list = [firms_dict, avg_profit_dict]
    print(firms_list)
with open(file_name_json, 'w') as out_file:
    json.dump(firms_list, out_file)
