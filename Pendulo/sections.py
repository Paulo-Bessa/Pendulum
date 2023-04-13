from poincare import poincare_section
from pendulo import model
from data import pend_data
from params import Omega
import numpy as np

data = pend_data()
pos,vel,ang,tmp = data.T
states = np.array([pos,vel]).T

def p_sections(num):
    total_points = []
    for numi in np.linspace(0,2*np.pi,num):
        pts=poincare_section(states, tmp, Omega,eps=numi)
        pts=np.array(pts).T
        total_points.append(pts)
    return total_points