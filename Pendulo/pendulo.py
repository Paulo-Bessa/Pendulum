import numpy as np

def model(x,t,args,F=0):
    zeta,I,k,d,D,m,g,a,b,q,Omega,mu = args
    K = (2/np.pi)*mu*np.arctan(q*x[1])
    
    one = x[1]
    force=(k*d/(2*I))*(np.sqrt(a**2 + b**2 - 2*a*b*np.cos(x[2])) - (a-b) - F)
    two = force - (zeta/I)*x[1] - (k*(d**2)/(2*I))*x[0] - K/I - (m*g*D*np.sin(x[0])/(2*I))
    three = Omega
    ans = np.array([one,two,three])
    return ans