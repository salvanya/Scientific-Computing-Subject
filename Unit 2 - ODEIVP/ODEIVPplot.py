import matplotlib.pyplot as plt
import numpy as np

file = open('data/data_to_plot.txt', 'r')
methods = file.readline().split()
order = int(file.readline())
file.close()

data = np.loadtxt('data/data_to_plot.txt', skiprows= 2)

# print(methods)
methods_quantity = len(methods)
methods_string = ''


# def compare_function(x,y=1):
#     func = -0.5*x**4 + 4*x**3 - 10*x**2 + 8.5*x + 1
#     return func

# comp_func = [[],[]]

# x_0 = 0
# x_end = 4
# x = x_0
# h = 0.1

# while x <= x_end:
#     comp_func[0] = x
#     comp_func[1] = compare_function(x)
#     x += h

# plt.plot(comp_func[0], comp_func[1], label = 'Analitic')


for index, method in enumerate(methods):
    for i in range(order):
        plt.plot(data[:,0], data[:,1+index*2+i], label = f'{method} y{i}')
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
