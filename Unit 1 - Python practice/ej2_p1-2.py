list = [3, 6, 8, 5, 3, 1, 2, 4, 5, 1, 2, 15, 7, 8, 0, 10]

print("\na) ------------------------\n")

for number in list:
    if number%2 == 0:
        print(number)

print("\nb) ------------------------\n")

for index, number in enumerate(list):
    if not index%2 == 0:
        print(number)

print("\nc) ------------------------\n")

for index, number in enumerate(reversed(list)):
    if index%2 == 0:
        print(number)
