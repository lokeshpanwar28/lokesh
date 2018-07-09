# This is the test example of the linear regration devloped by the lokesh and also verified with the existing method in the python
import numpy as np
xx = np.array([[1988,183800],
[1989,183200],
[1990,174900],
[1991,173500],
[1992,172900],
[1993,173200],
[1994,173200],
[1995,169700],
[1996,174500],
[1997,177900],
[1998,188100],
[1999,203200],
[2000,230200],
[2001,258200],
[2002,309800],
[2003,329800]])
N = len(xx)
x=xx[:,0]/2000
y=xx[:,1]/320000
all_fun=np.zeros(30)
all_m=np.zeros([30,2])
max_iter=5000
for j in range(1,30):
    m = np.random.rand(2)
    for i in range(0,max_iter):
        # defining the slop of the cost function
         m -= (0.03/N)*np.array([sum((m[0]*x+m[1]*np.ones(N)-y)*x),sum((m[0]*x+m[1]*np.ones(N)-y))],dtype=float)
         # function calculation end of the all iteration
         fun = sum((m[0]*x+m[1]*np.ones(N)-y)**2)
    all_fun[j]=fun
    all_m[j,:]=m
# show the 30 vale generated with this gradient based method
print all_fun[1:],all_m[1:,:]


# nelder method for optimization
from scipy.optimize import minimize

def rosen(m):
    return sum((m[0]*x+m[1]*np.ones(N)-y)**2)
    
m0=np.array([0,0])
res = minimize(rosen, m0, method='nelder-mead',options={'xtol': 1e-8, 'disp': True})
print res.fun,res.x

#print fun-res.fun