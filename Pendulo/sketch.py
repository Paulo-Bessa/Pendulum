from numpy import array, arange, zeros, dot, log
import matplotlib.pyplot as plt
from numpy.linalg import norm

# Evolution equation of tracjectories and tangential vectors
def f(r):
    x = r[0]
    y = r[1]
    z = r[2]

    fx = sigma * (y - x)
    fy = x * (rho - z) - y
    fz = x * y - beta * z

    return array([fx,fy,fz], float)

def jacobian(r):
    M = zeros([3,3])
    M[0,:] = [- sigma, sigma, 0]
    M[1,:] = [rho - r[2], -1, - r[0] ]
    M[2,:] = [r[1], r[0], -beta]

    return M

def g(d, r):
    dx = d[0]
    dy = d[1]
    dz = d[2]

    M = jacobian(r)

    dfx = dot(M, dx)
    dfy = dot(M, dy)
    dfz = dot(M, dz)

    return array([dfx, dfy, dfz], float)

# Initial conditions
d = array([[1,0,0], [0,1,0], [0,0,1]], float)
r = array([19.0, 20.0, 50.0], float)
sigma, rho, beta = 16, 45.92, 4.0 

T  = 10**5                         # time steps 
dt = 0.01                          # time increment
Teq = 10**4                        # Transient time

l1, l2, l3 = 0, 0, 0               # Lengths

xpoints, ypoints, zpoints  = [], [], []

# Transient
for t in range(Teq):
    # RK4 - Method 
    k1  = dt * f(r)                 
    k11 = dt * g(d, r)

    k2  = dt * f(r + 0.5 * k1)
    k22 = dt * g(d + 0.5 * k11, r + 0.5 * k1)

    k3  = dt * f(r + 0.5 * k2)
    k33 = dt * g(d + 0.5 * k22, r + 0.5 * k2)

    k4  = dt * f(r + k3)
    k44 = dt * g(d + k33, r + k3)

    r  += (k1  + 2 * k2  + 2 * k3  + k4)  / 6
    d  += (k11 + 2 * k22 + 2 * k33 + k44) / 6

    # Gram-Schmidt-Scheme
    orth_1 = d[0]                    
    d[0] = orth_1 / norm(orth_1)

    orth_2 = d[1] - dot(d[1], d[0]) * d[0]
    d[1] = orth_2 / norm(orth_2)

    orth_3 = d[2] - (dot(d[2], d[1]) * d[1]) - (dot(d[2], d[0]) * d[0]) 
    d[2] = orth_3 / norm(orth_3)

for t in range(T):
    k1  = dt * f(r)                 
    k11 = dt * g(d, r)

    k2  = dt * f(r + 0.5 * k1)
    k22 = dt * g(d + 0.5 * k11, r + 0.5 * k1)

    k3  = dt * f(r + 0.5 * k2)
    k33 = dt * g(d + 0.5 * k22, r + 0.5 * k2)

    k4  = dt * f(r + k3)
    k44 = dt * g(d + k33, r + k3)

    r  += (k1  + 2 * k2  + 2 * k3  + k4)  / 6
    d  += (k11 + 2 * k22 + 2 * k33 + k44) / 6

    orth_1 = d[0]                    # Gram-Schmidt-Scheme
    l1 += log(norm(orth_1))/log(2)
    d[0] = orth_1 / norm(orth_1)

    orth_2 = d[1] - dot(d[1], d[0]) * d[0]
    l2 += log(norm(orth_2))/log(2)
    d[1] = orth_2 / norm(orth_2)

    orth_3 = d[2] - (dot(d[2], d[1]) * d[1]) - (dot(d[2], d[0]) * d[0]) 
    l3 += log(norm(orth_3))/log(2)
    d[2] = orth_3 / norm(orth_3)

# Correct Solution (2.16, 0.0, -32.4)

lya1 = l1 / (dt * T)
lya2 = l2 / (dt * T)  - lya1
lya3 = l3 / (dt * T) -  lya1 - lya2 

print(lya1)
print(lya2)
print(lya3)

# my solution T = 10^5 : (1.3540301507934012, -0.0021967491623752448, -16.351653561383387) 