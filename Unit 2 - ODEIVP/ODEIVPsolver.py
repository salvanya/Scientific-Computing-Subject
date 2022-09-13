from data.function import f
from data.methods import euler, midpoint, heun, rk4
import numpy as np

config = np.loadtxt('data/configuration.txt', comments = '#', dtype = 'str')

h = float( config[0] )
x_0 = float( config[1] )
x_end = float( config[2] )

order = int( config[3] )
initial_conditions = []
for i in range( order ):
    initial_conditions.append( float( config[4+i] ) )

number_of_methods = int( config[4+order] )
methods = []
for i in range( number_of_methods ):
    methods.append( config[5+order+i] )


# print(f'h = {h}\n\
# x_0 = {x_0}\n\
# x_end = {x_end}\n\
# order = {order}\n\
# initial_conditions = {initial_conditions}\n\
# number_of_methods = {number_of_methods}\n\
# methods = {methods}\n')

methods_to_write = ''

x = np.linspace(x_0, x_end, int(((x_end - x_0)/h)))    
Y_i = initial_conditions[0] 
data = {}
x = np.nditer(x, flags=['f_index'])
x.iternext()
x_1 = x.iternext()

for method in methods:
    data[method] = [initial_conditions[0]]
    
    if method == 'euler':
        data[method].append(euler(initial_conditions[0], x_1, h))
        methods_to_write += 'Euler '
    
    elif method == 'midpoint':
        data[method].append(midpoint(initial_conditions[0], x_1, h))
        methods_to_write += 'Midpoint '    

    elif method == 'heun':
        data[method].append(heun(initial_conditions[0], x_1, h))
        methods_to_write += 'Heun '    
    
    
    elif method == 'rk4':
        data[method].append(rk4(initial_conditions[0], x_1, h))
        methods_to_write += 'RK4 '    


    globals()[f'y_{method}'] = data[method][1]


for x_i in x:
    for method in methods:
        if method == 'euler':
            y_euler = euler(y_euler, x_i, h)
            data[method].append(y_euler)
                            
        if method == 'midpoint':
            y_midpoint = midpoint(y_midpoint, x_i, h)
            data[method].append(y_midpoint)

        if method == 'heun':
            y_heun = heun(y_heun, x_i, h)
            data[method].append(y_heun)

        if method == 'rk4':
            y_rk4 = rk4(y_rk4, x_i, h)
            data[method].append(y_rk4)
        

file = open('data/data_to_plot.txt', 'w')
file.write(methods_to_write + '\n')
file.close

file = open('data/data_to_plot.txt', 'a')

data_length = np.linspace(x_0, x_end, int(((x_end - x_0)/h)))

for index, x_i in enumerate(data_length):
    row = str(x_i)
    
    for method in methods:
        row += " " + str(data[method][index]) 

    row += "\n"
    file.write(row)

file.close() 