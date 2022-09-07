import numpy as np
import matplotlib.pyplot as plt
from function import func as f

file = open("euler_data.txt")

data = {}

while True:
    line = file.readline().split()
    if line == []:
        break
    data[line[0]] = line[1]

file.close()

