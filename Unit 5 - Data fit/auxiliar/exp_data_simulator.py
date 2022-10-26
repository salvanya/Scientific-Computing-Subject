import numpy as np
import random as rand

def exp_data_simulator(start, stop, func, var):
    '''exp_data_simulator[start, stop, function, variability)
       start[float]: Interval start 
       stop[float]: Interval Stop
       function[function y=f(x)]: Function to simulate 
       variability[float]: Maximum variability of the data point 
       '''
       
    x = np.linspace(start,stop)
    y=[]
    
    for x_i in x:
        y.append( func(x_i) + rand.uniform(-var,var) )
    
    return (x,y)
