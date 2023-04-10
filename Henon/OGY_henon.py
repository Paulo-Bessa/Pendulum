import numpy as np
from henon import *
from OPI import distance

def OGY_control(init,UPO,ns = 1e5,reference_parameter=1.4,tol=2e-2):
    if not isinstance(init,np.ndarray):
        init = np.array(init)
    if not isinstance(UPO,np.ndarray):
        UPO  = np.array(UPO)

    parameter = reference_parameter
    points_nc = [init]
    points_c  = [init]
    counter = 0
    for i in range(int(ns)):
        if parameter!=1.4:
            print(parameter)
        if distance(init,UPO)<tol:
            J = Jacobian_henon(UPO[counter])
            w = DF_Dparameter(UPO[counter])

            dxi = init - UPO[counter]
            dxi = np.reshape(dxi,(2,1))
            dp  = parameter - reference_parameter

            eigval,eigvec = np.linalg.eig(J)
            directions = np.linalg.pinv(eigvec).T

            dxi_iter = J@dxi + w*dp

            for i in range(2):
                if eigval[i]>0:
                    correct_val = eigval[i]
                    correct_dir = directions[i]
            correct_dir = np.reshape(correct_dir,(1,2))
            dp_iter = -correct_val * (correct_dir@dxi_iter)/(correct_dir@w)
            if dp_iter[0][0]<9e-2:
                parameter += dp_iter[0][0]
            counter+=1

            if counter>=len(UPO):
                counter=0
        init_c = henon_step(init[0],init[1],a=parameter)
        init_nc= henon_step(init[0],init[1],a=reference_parameter)
        points_c.append(init_c)
        points_nc.append(init_nc)
        init = init_c
    points_c=np.array(points_c)
    return points_c.T
