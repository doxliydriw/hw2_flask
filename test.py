# f = open("demofile.txt", "r")
# for x in f:
#   print(x)

# with open('requirements.txt', 'r') as file:
#     lines = file.readlines()
#     data = "".join(lines)
# print(data)

# from faker import Faker
# fake = Faker()
# for user in range(10):
#   username = fake.name()
#   username = username.split(' ')
#   company = fake.company().split(' ')
#   print(f'{str(username[0])[0].lower()}.{str(username[1]).lower()}@{str(company[0]).lower()}.com')


# import csv
# import statistics
# weight = []
# height = []
# with open('hw.csv', newline='') as file:
#     reader = csv.reader(file, delimiter=',', quotechar=',')
#     next(reader)
#     for row in reader:
#         # print(row)
#         if row:
#             height.append(float(row[1]))
#             weight.append(float(row[2]))
#     print(f' Avarage height is: {statistics.mean(height) * 2.54} cm')
#     print(f' Avarage weight is: {statistics.mean(height) * 0.45359237} kgs')

#     # storing all the rows in an output list
#     output = []
#     for row in reader:
#         output.append(row[:])
#
# for rows in range[10]:
#     print(rows)

import requests
r = requests.get('http://api.open-notify.org/astros.json')
answer = r.json().get('number')
print(f'Currently there are {answer} astronauts')
