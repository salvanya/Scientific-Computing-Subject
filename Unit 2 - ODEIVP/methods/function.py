import numpy as np

def f(x, y=0):
    func = np.zeros(2)
    
    func[0] = y[1]
    func[1] = x*(y[0]**2)
    
    return func

# y = np.zeros(2)

# y[0] = 2
# y[1] = 3

# print(f(1,y))