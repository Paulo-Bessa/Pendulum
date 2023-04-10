import numpy as np
from duffing import *
from OPI import distance
from Lyapunov.runge_kutta import *

def OGY_control(init,UPO,t0,tmax,step=1e-3,freq=0.5,reference_parameter=7.5,tol=2):
    if not isinstance(init,np.ndarray):
        init = np.array(init)
    if not isinstance(UPO,np.ndarray):
        UPO  = np.array(UPO)

    parameter = reference_parameter
    points_c  = [init]
    poincare  = []
    counter = 0

    passa=0
    
    while t0<=tmax:
        if (t0)%(2*np.pi*freq)<tol:
            # Poincare
            poincare.append(([init,t0]))
            # Control
            if distance(init,UPO)<tol:
                passa+=1
                print(passa)
                J = Jacobian_duf(UPO[counter],t0)
                w = DF_Dparameter(UPO[counter],t0)

                dxi = init - UPO[counter]
                dxi = np.reshape(dxi,(2,1))
                dp  = parameter - reference_parameter

                eigval,eigvec = np.linalg.eig(J)
                directions = np.linalg.pinv(eigvec).T

                dxi_iter = J@dxi + w*dp

                for i in range(2):
                    print(eigval[i])
                    if eigval[i]>0:
                        correct_val = eigval[i]
                        correct_dir = directions[i]
                correct_dir = np.reshape(correct_dir,(1,2))
                dp_iter = -correct_val * (correct_dir@dxi_iter)/(correct_dir@w)
                if dp_iter[0][0]<8e-1:
                    parameter += dp_iter[0][0]
                counter+=1

                if counter>=len(UPO):
                    counter=0
        # Update            
        if parameter!=7.5:
            print(parameter)
        f = lambda y,t:duf_osc(y,t,mu=parameter)
        init,t0 = rk4_step(f,init,t0,h=step)
        points_c.append(init)



    # points = []
    # ans=np.array(ans)
    # for i in range(len(time)):
    #     if (time[i]+eps)%(2*np.pi*freq)<tol:
    #         points.append((ans.T)[i])

    
    # init_c = henon_step(init[0],init[1],a=parameter)
    # init_nc= henon_step(init[0],init[1],a=reference_parameter)
    # points_c.append(init_c)
    # points_nc.append(init_nc)
    # init = init_c
    # points_c=np.array(points_c)
    return points_c
