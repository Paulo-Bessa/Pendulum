from sections import p_sections
import matplotlib.pyplot as plt

NUM = 4
sections = p_sections(NUM)

fig,axs = plt.subplots(nrows=2,ncols=2)
axs[0][0].plot(sections[0][0],sections[0][1],"o",markersize=2)
axs[0][1].plot(sections[1][0],sections[1][1],"o",markersize=2)
axs[1][0].plot(sections[2][0],sections[2][1],"o",markersize=2)
axs[1][1].plot(sections[3][0],sections[3][1],"o",markersize=2)
plt.show()