from sections import p_sections
import matplotlib.pyplot as plt
from pyragas import pyrag
import numpy as np

P = 2
# Para P=2 e ganho 0.7, obtivemos uma estabilização em torno de uma OPI de período 3

y0=np.array([1,1,1])
t0=0
tmax=350
h=1e-2
k1,k2,k3,k4,k5,k6,k7,k8,k9 = np.linspace(0.05,0.25,9)
# k1=1.8
# k2=1.85
# k3=1.9
# k4=1.95
# k5=2.0
# k6=2.05
# k7=2.1
# k8=2.15
# k9=2.2
time1,ans1 = pyrag(k1,P,y0,t0,tmax,h)
time2,ans2 = pyrag(k2,P,y0,t0,tmax,h)
time3,ans3 = pyrag(k3,P,y0,t0,tmax,h)
time4,ans4 = pyrag(k4,P,y0,t0,tmax,h)
time5,ans5 = pyrag(k5,P,y0,t0,tmax,h)
time6,ans6 = pyrag(k6,P,y0,t0,tmax,h)
time7,ans7 = pyrag(k7,P,y0,t0,tmax,h)
time8,ans8 = pyrag(k8,P,y0,t0,tmax,h)
time9,ans9 = pyrag(k9,P,y0,t0,tmax,h)

# NUM = 4
# sections = p_sections(NUM)
PRIM=15000
fig,axs = plt.subplots(nrows=3,ncols=3)
axs[0][0].set_title("Gain %.3f"%(k1))
axs[0][1].set_title("Gain %.3f"%(k2))
axs[0][2].set_title("Gain %.3f"%(k3))
axs[1][0].set_title("Gain %.3f"%(k4))
axs[1][1].set_title("Gain %.3f"%(k5))
axs[1][2].set_title("Gain %.3f"%(k6))
axs[2][0].set_title("Gain %.3f"%(k7))
axs[2][1].set_title("Gain %.3f"%(k8))
axs[2][2].set_title("Gain %.3f"%(k9))
axs[0][0].plot(ans1[0][PRIM:],ans1[1][PRIM:],linewidth=0.3)
axs[0][1].plot(ans2[0][PRIM:],ans2[1][PRIM:],linewidth=0.3)
axs[0][2].plot(ans3[0][PRIM:],ans3[1][PRIM:],linewidth=0.3)
axs[1][0].plot(ans4[0][PRIM:],ans4[1][PRIM:],linewidth=.3)
axs[1][1].plot(ans5[0][PRIM:],ans5[1][PRIM:],linewidth=.3)
axs[1][2].plot(ans6[0][PRIM:],ans6[1][PRIM:],linewidth=.3)
axs[2][0].plot(ans7[0][PRIM:],ans7[1][PRIM:],linewidth=.3)
axs[2][1].plot(ans8[0][PRIM:],ans8[1][PRIM:],linewidth=.3)
axs[2][2].plot(ans9[0][PRIM:],ans9[1][PRIM:],linewidth=.3)

# axs[0][0].plot(time1[PRIM:],ans1[1][PRIM:],linewidth=0.3)
# axs[0][1].plot(time2[PRIM:],ans2[1][PRIM:],linewidth=0.3)
# axs[0][2].plot(time3[PRIM:],ans3[1][PRIM:],linewidth=0.3)
# axs[1][0].plot(time4[PRIM:],ans4[1][PRIM:],linewidth=.3)
# axs[1][1].plot(time5[PRIM:],ans5[1][PRIM:],linewidth=.3)
# axs[1][2].plot(time6[PRIM:],ans6[1][PRIM:],linewidth=.3)
# axs[2][0].plot(time7[PRIM:],ans7[1][PRIM:],linewidth=.3)
# axs[2][1].plot(time8[PRIM:],ans8[1][PRIM:],linewidth=.3)
# axs[2][2].plot(time9[PRIM:],ans9[1][PRIM:],linewidth=.3)
plt.show()