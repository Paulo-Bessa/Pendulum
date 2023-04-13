from matplotlib import pyplot as plt
from poincare import poincare_section
from csv import reader
import numpy as np

OMEGA = 1

position=[]
velocity=[]
time=[]

with open('NOVO1.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        position.append(float(row[0]))
        velocity.append(float(row[1]))
        time.append(float(row[2]))

ans = [position,velocity]

sections = []
NUM=64
for i in range(2*NUM):
    elem = poincare_section(ans,time,OMEGA,eps=i*2*np.pi/NUM)
    elem = elem.T
    sections.append(elem)

x = []
y = []
  

plt.figure(figsize=(10,6))
for section in sections:
  
    # Mention x and y limits to define their range
    plt.xlim(-4.5, 4.5)
    plt.ylim(-7, 7)
      
    # Ploting graph
    plt.plot(section[0], section[1],".",markersize=2, color = 'green')
    plt.pause(0.05)
    plt.clf()
  
plt.show()