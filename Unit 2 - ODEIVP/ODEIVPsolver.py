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

for method in methods:
    if method == 'euler':
        data_euler = euler(f, x_0, x_end, h, initial_conditions[0])
        methods_to_write += 'Euler '    
        
    if method == 'midpoint':
        data_midpoint = midpoint(f, x_0, x_end, h, initial_conditions[0])
        methods_to_write += 'Midpoint '

    if method == 'heun':
        data_heun = heun(f, x_0, x_end, h, initial_conditions[0])
        methods_to_write += 'Heun '

    if method == 'rk4':
        data_rk4 = rk4(f, x_0, x_end, h, initial_conditions[0])
        methods_to_write += 'RK4 '

file = open('data/data_to_plot.txt', 'w')
file.write(methods_to_write + '\n')
file.close

file = open('data/data_to_plot.txt', 'a')

data_length = np.linspace(x_0, x_end, int(((x_end - x_0)/h)))

for index, x_i in enumerate(data_length):
    row = str(x_i)
    
    for method in methods:
        row += " " + str(globals()[f'data_{method}'][1][index]) 

    row += "\n"
    file.write(row)

file.close() 