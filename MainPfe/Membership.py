import skfuzzy as fuzz
import numpy as np
import matplotlib.pyplot as plt 

x = np.arange(0 , 1.01 , 0.01)
x2 = np.arange(1 , 100)
circularite  = fuzz.trapmf(x, [0 ,0 , 0.45 , 0.65 ])
excentricite  = fuzz.trapmf(x, [0.55 ,0.75 , 1 , 1 ])
compacite  = fuzz.trapmf(x, [0.38 ,0.55 , 0.92 , 1 ])
Rectangularite  = fuzz.trapmf(x, [0.4 ,0.52 , 0.72 , .8 ])

Age = fuzz.trapmf(x2, [30 , 44 , 75 , 90])

def getCr(xx) :
    y = fuzz.interp_membership(x , circularite , xx)
    return  y if y!=1 else abs(y - 0.05)

def getEx(xx) :
    y = fuzz.interp_membership(x , excentricite , xx)
    return  y if y!=1 else abs(y - 0.05)

def getCo(xx) :
    y = fuzz.interp_membership(x , compacite , xx)
    return  y if y!=1 else abs(y - 0.05)

def getRc(xx) :
    y = fuzz.interp_membership(x , Rectangularite , xx)
    return  y if y!=1 else abs(y - 0.05)

def getAge(xx) :
    y = fuzz.interp_membership(x2 , Age , xx)
    return  y if y!=1 else abs(y - 0.05)



