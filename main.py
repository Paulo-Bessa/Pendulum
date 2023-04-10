from Lyapunov.runge_kutta import *
from poincare import poincare_section
from duffing import duf_osc, Jacobian_duf, DF_Dparameter
from OPI import identify_UPO,modulo_UPO,distance
from SC_duffing import control_sc
import matplotlib.pyplot as plt
import numpy as np
import time as tm

start_time = tm.time()

control_sc()

# ALPHA=0.05
# GAMMA=-0.2
# BETA=1
# OMEGA=1
# MU=7.5
# PERIOD2= 2
# init = [1,1]
# position=[]
# velocity=[]
# time=[]

# ## OFFLINE LEARNING

# with open('NOVO1.csv', 'r') as read_obj:
#     # pass the file object to reader() to get the reader object
#     csv_reader = reader(read_obj)
#     # Iterate over each row in the csv using reader object
#     for row in csv_reader:
#         # row variable is a list that represents a row in csv
#         position.append(float(row[0]))
#         velocity.append(float(row[1]))
#         time.append(float(row[2]))

# ans = [position,velocity]
# sections = []
# for freq in np.linspace(0,2*np.pi,8):
#     section = poincare_section(ans,time,OMEGA,eps=freq)
#     # print(np.shape(section))
#     sections.append(section)

# TOL1 = 4e-2
# TOL2 = 1e-1
# section = poincare_section(ans,time,OMEGA)
# prox2 = identify_UPO(section,PERIOD2,tol=TOL1)
# proximities2 = modulo_UPO(prox2,section,tol=TOL2)

# NUM=prox2[0]

# sections_UPO = [elem[NUM] for elem in sections]


## ONLINE

# tmax = 10
# t0 = 0
# step = 1e-3
# init = np.array([1,1])
# eps = 0
# tol = 2e-3
# rad_trap = 5e-2

# alpha=ALPHA
# gamma=GAMMA
# beta=BETA
# mu=MU
# omega=OMEGA

# mus = np.linspace(3.7,7.8,3000)
# VALS=[]
# for NUS in mus:
#     INOT=np.random.random(2)
#     FUNC = lambda x,t:duf_osc(x,t,mu=NUS)
#     timeq,ansq=runge_kutta_integrator(FUNC,INOT,0,50,step=2e-2)
#     sectionq = poincare_section(ansq,timeq,OMEGA)
#     print(sectionq[-1])
#     VALS.append(sectionq[-1][0])
# plt.plot(mus,VALS,"o",markersize=2)
# plt.show()


print("--- %s seconds ---" % (tm.time() - start_time))

