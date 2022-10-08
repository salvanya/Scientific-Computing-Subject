import numpy as np

def f(x, Y):
    func = np.zeros(2)
    func[0] = Y[1]    
    func[1] = -Y[0]
    
    return func