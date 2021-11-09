import numpy as np
import matplotlib.pyplot as ptl

def interpolLineal():
    X = np.linspace(-np.pi,np.pi,5)
    Xexp=np.linspace(-np.pi,np.pi,21)
    Yexp = np.sin(Xexp)

    Y = np.interp(X,Xexp,Yexp)

    ptl.plot(Xexp, Yexp)
    ptl.plot(X, Y, 'r -')
    ptl.show()