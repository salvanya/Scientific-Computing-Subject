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


print(f'h = {h}\n\
x_0 = {x_0}\n\
x_end = {x_end}\n\
order = {order}\n\
initial_conditions = {initial_conditions}\n\
number_of_methods = {number_of_methods}\n\
methods = {methods}\n')

methods_to_write = ''

Y_i = initial_conditions
data = {}
data['x'] = [x_0]
x = x_0

for method in methods:
    data[method] = [initial_conditions]
    
    if method == 'euler':
        methods_to_write += 'Euler '
    
    elif method == 'midpoint':
        methods_to_write += 'Midpoint '    

    elif method == 'heun':
        methods_to_write += 'Heun '    
    
    elif method == 'rk4':
        methods_to_write += 'RK4 '    

while x <= x_end:

    index = data['x'].index(x)

    for method in methods:
        if method == 'euler':
            data[method].append(euler(x, data['euler'][index], h))
                            
        if method == 'midpoint':
            data[method].append(midpoint(x, data['midpoint'][index], h))

        if method == 'heun':
            data[method].append(heun(x, data['heun'][index], h))

        if method == 'rk4':
            data[method].append(rk4(x, data['rk4'][index], h))

    x += h
    data['x'].append(x)
    
file = open('data/data_to_plot.txt', 'w')
file.write(methods_to_write + '\n' + str(order) + '\n')
file.close

file = open('data/data_to_plot.txt', 'a')


for index, x in enumerate(data['x']):
    row = str(x)
    
    for method in methods:
        for i in range(order):
            row += " " + str(data[method][index][i]) 

    row += "\n"
    file.write(row)


file.close() 
#print(data)