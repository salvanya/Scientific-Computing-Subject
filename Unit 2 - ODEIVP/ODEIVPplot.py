import matplotlib.pyplot as plt
import numpy as np

file = open('data/data_to_plot.txt', 'r')
methods = file.readline().split()
file.close()

data = np.loadtxt('data/data_to_plot.txt', skiprows= 1)

# print(methods)
methods_quantity = len(methods)
methods_string = ''

for index, method in enumerate(methods):
    plt.plot(data[:,0], data[:,index+1], label = method)
    if methods_quantity > 1:
        if index < ( methods_quantity - 2 ):
            methods_string += method + 'and '
        elif index == ( methods_quantity - 1 ):
            methods_string += method
        else:
            methods_string += method + ', '
    else:
        methods_string += method

plt.xlabel (r'$x$')
plt.ylabel (r'$y(x)$')
plt.title(f"ODE IVP solution by {methods_string} methods")

plt.legend(loc='best')

plt.show()
plt.savefig('data/solution.pdf')
