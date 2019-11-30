import numpy as np

X= np.zeros((10,10))
S= 0
for Y in range(10):
    for Z in range(10):
        S +=1
        X[Y,Z]= S**2
        
        dive3 = X[X%3==0]