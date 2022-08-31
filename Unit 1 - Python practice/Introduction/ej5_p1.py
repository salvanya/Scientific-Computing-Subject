list = [23.33, 8.08, 44.99, 21.95, 44.93, 29.82, 41.08, 28.57, 4.39, 43.79, 20.02, 26.59, 41.13, 39.32, 26.85]

for number in list:
        if number < minimum:
            minimum = number

print (minimum)

orderedList = []

while len(list):
    minimum=list[0]
    for number in list:
        if number < minimum:
            minimum = number
    orderedList.append(minimum)
    list.remove(minimum)

print(orderedList)
     