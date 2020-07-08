import re

handle = open('regex_sum_711699.txt')

num_all = []
for line in handle:
    line = line.rstrip()
    num_list = re.findall('[0-9]+', line)
    if len(num_list) >= 1:
        for i in range(len(num_list)):
            num = int(num_list[i])
            num_all.append(num)

print('Sum of the numbers in the file:', sum(num_all))
