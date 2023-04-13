import pygame
import sys
from pygame.locals import *
from math import pi, cos, sin
import numpy as np
import matplotlib.pyplot as plt

a = 1.4
b = 0.3
# def henon(x):
#     x1 = 1 - a*x[0]*x[0] + x[1]
#     x2 = b*x[0]
#     return np.array([x1,x2])

w, h = 600,600
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LT_BLUE = (230,230,255)

screen = pygame.display.set_mode((w,h))
screen.fill(BLACK)
trace = screen.copy()
pygame.display.update()
clock = pygame.time.Clock()

pygame.draw.line(screen, WHITE, (0,h/2),(w,h/2),1)
pygame.draw.line(screen, WHITE, (w/2,0),(w/2,h),1)

# balls_loc = []
# balls_operated = []
# balls_reverse = []

# balls_operated2 = []
# balls_reverse2 = []

# balls_operated3 = []
# balls_reverse3 = []

# balls_operated4 = []
# balls_reverse4 = []

# balls_operated5 = []
# balls_reverse5 = []

# balls_operated6 = []
# balls_reverse6 = []

# balls_operated7 = []
# balls_reverse7 = []

# balls_operated8 = []
# balls_reverse8 = []

N = 10
# n=0.9

# for i in range(N):
#     for j in range(N):
#         balls_loc.append((230+j*10,30+i*10))

# balls_loc = np.array(balls_loc)

# First iteration
# for ball in balls_loc:
#     op = (ball-np.array([w/2,h/2]))
#     scale = op*(n/400)
#     balls_operated.append(henon(scale))

# for ball in balls_operated:
#     balls_reverse.append(ball*(400/n) + np.array([w/2,h/2]))

# Second iteration
# for ball in balls_reverse:
#     op = (ball-np.array([w/2,h/2]))
#     scale = op*(n/400)
#     balls_operated2.append(henon(scale))

# for ball in balls_operated2:
#     balls_reverse2.append(ball*(400/n) + np.array([w/2,h/2]))

# Third iteration
# for ball in balls_reverse2:
#     op = (ball-np.array([w/2,h/2]))
#     scale = op*(n/400)
#     balls_operated3.append(henon(scale))

# for ball in balls_operated3:
#     balls_reverse3.append(ball*(400/n) + np.array([w/2,h/2]))

# Fourth iteration
# for ball in balls_reverse3:
#     op = (ball-np.array([w/2,h/2]))
#     scale = op*(n/400)
#     balls_operated4.append(henon(scale))

# for ball in balls_operated4:
#     balls_reverse4.append(ball*(400/n) + np.array([w/2,h/2]))

# Fifth iteration
# for ball in balls_reverse4:
#     op = (ball-np.array([w/2,h/2]))
#     scale = op*(n/400)
#     balls_operated5.append(henon(scale))

# for ball in balls_operated5:
#     balls_reverse5.append(ball*(400/n) + np.array([w/2,h/2]))

# Sixth iteration
# for ball in balls_reverse5:
#     op = (ball-np.array([w/2,h/2]))
#     scale = op*(n/400)
#     balls_operated6.append(henon(scale))

# for ball in balls_operated6:
#     balls_reverse6.append(ball*(400/n) + np.array([w/2,h/2]))

# Seventh iteration
# for ball in balls_reverse6:
#     op = (ball-np.array([w/2,h/2]))
#     scale = op*(n/400)
#     balls_operated7.append(henon(scale))

# for ball in balls_operated7:
#     balls_reverse7.append(ball*(400/n) + np.array([w/2,h/2]))

# Eighth iteration
# for ball in balls_reverse7:
#     op = (ball-np.array([w/2,h/2]))
#     scale = op*(n/400)
#     balls_operated8.append(henon(scale))

# for ball in balls_operated8:
#     balls_reverse8.append(ball*(400/n) + np.array([w/2,h/2]))

t = 1.3
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # for ball in balls_reverse:
    # pygame.draw.circle(screen, WHITE, (int(ball[0]),int(ball[1])),5)
    screen.fill(BLACK)
    if t<1.42:
        t+=2e-3
    else:
        pass
    # print("O valor de t eh: "+str(t)+"\n")
    def henon_attractor(x, y, a=t, b=0.3):
        '''Computes the next step in the Henon 
        map for arguments x, y with kwargs a and
        b as constants.
        '''
        x_next = 1 - a * x ** 2 + y
        y_next = b * x
        return x_next, y_next

    # number of iterations and array initialization
    steps = 60000
    X = np.zeros(steps + 1)
    Y = np.zeros(steps + 1)

    # starting point
    X[0], Y[0] = 0, 0

    # add points to array
    for i in range(steps):
        x_next, y_next = henon_attractor(X[i], Y[i])
        X[i+1] = x_next
        Y[i+1] = y_next
        # print("Os valores sao: "+str(x_next)+" e "+str(y_next)+"\n")
        # pygame.draw.circle(screen, RED, (200,200),20)
        scale = 200
        exp_x,exp_y = int(x_next*scale+w/2),int(y_next*scale+h/2)
        # print("Os valores de a e b sao: "+str(t)+" e "+str(0.3)+"\n")
        pygame.draw.circle(screen, WHITE, (exp_x,exp_y),1)

        # plot figure
        # plt.figure(figsize=(9,9))
        # plt.plot(X, Y, '^', color='white', alpha = 0.8, markersize=0.3)
        # plt.axis('off')
        # plt.show()
        # plt.close()
        # if i%100==0:
        #     print("O valor de i eh: "+str(i)+"\n")
        # if i == 1300 or i == 1301:
        #     if t<1:
        #         pygame.draw.circle(screen, RED, (int(balls_loc[i][0]*(1-t) + balls_reverse[i][0]*t),int(balls_loc[i][1]*(1-t) + balls_reverse[i][1]*t)),5)
        #     elif t>=1 and t<2:
        #         pygame.draw.circle(screen, RED, (int(balls_reverse[i][0]*(2-t) + balls_reverse2[i][0]*(t-1)),int(balls_reverse[i][1]*(2-t) + balls_reverse2[i][1]*(t-1))),5)
        #     elif t>=2 and t<3:
        #         pygame.draw.circle(screen, RED, (int(balls_reverse2[i][0]*(3-t) + balls_reverse3[i][0]*(t-2)),int(balls_reverse2[i][1]*(3-t) + balls_reverse3[i][1]*(t-2))),5)
        #     elif t>=3 and t<4:
        #         pygame.draw.circle(screen, RED, (int(balls_reverse3[i][0]*(4-t) + balls_reverse4[i][0]*(t-3)),int(balls_reverse3[i][1]*(4-t) + balls_reverse4[i][1]*(t-3))),5)
        #     elif t>=4 and t<5:
        #         pygame.draw.circle(screen, RED, (int(balls_reverse4[i][0]*(5-t) + balls_reverse5[i][0]*(t-4)),int(balls_reverse4[i][1]*(5-t) + balls_reverse5[i][1]*(t-4))),5)
        #     elif t>=5 and t<6:
        #         pygame.draw.circle(screen, RED, (int(balls_reverse5[i][0]*(6-t) + balls_reverse6[i][0]*(t-5)),int(balls_reverse5[i][1]*(6-t) + balls_reverse6[i][1]*(t-5))),5)
        #     elif t>=6 and t<7:
        #         pygame.draw.circle(screen, RED, (int(balls_reverse6[i][0]*(7-t) + balls_reverse7[i][0]*(t-6)),int(balls_reverse6[i][1]*(7-t) + balls_reverse7[i][1]*(t-6))),5)
        #     elif t>=7 and t<8:
        #         pygame.draw.circle(screen, RED, (int(balls_reverse7[i][0]*(8-t) + balls_reverse8[i][0]*(t-7)),int(balls_reverse7[i][1]*(8-t) + balls_reverse8[i][1]*(t-7))),5)
        # else:
        #     if t<1:
        #         if abs(int(balls_loc[i][0]*(1-t) + balls_reverse[i][0]*t)) > 1e6:
        #             pass
        #         else:
        #             pygame.draw.circle(screen, WHITE, (int(balls_loc[i][0]*(1-t) + balls_reverse[i][0]*t),int(balls_loc[i][1]*(1-t) + balls_reverse[i][1]*t)),2)
        #     elif t>=1 and t<2:
        #         if abs(int(balls_reverse[i][0]*(2-t) + balls_reverse2[i][0]*(t-1))) > 1e6:
        #             pass
        #         else:
        #             pygame.draw.circle(screen, WHITE, (int(balls_reverse[i][0]*(2-t) + balls_reverse2[i][0]*(t-1)),int(balls_reverse[i][1]*(2-t) + balls_reverse2[i][1]*(t-1))),2)
        #     elif t>=2 and t<3:
        #         if abs(int(balls_reverse2[i][0]*(3-t) + balls_reverse3[i][0]*(t-2))) > 1e6:
        #             pass
        #         else:
        #             pygame.draw.circle(screen, WHITE, (int(balls_reverse2[i][0]*(3-t) + balls_reverse3[i][0]*(t-2)),int(balls_reverse2[i][1]*(3-t) + balls_reverse3[i][1]*(t-2))),2)
        #     elif t>=3 and t<4:
        #         if abs(int(balls_reverse3[i][0]*(4-t) + balls_reverse4[i][0]*(t-3))) > 1e6:
        #             pass
        #         else:
        #             pygame.draw.circle(screen, WHITE, (int(balls_reverse3[i][0]*(4-t) + balls_reverse4[i][0]*(t-3)),int(balls_reverse3[i][1]*(4-t) + balls_reverse4[i][1]*(t-3))),2)
        #     elif t>=4 and t<5:
        #         if abs(int(balls_reverse4[i][0]*(5-t) + balls_reverse5[i][0]*(t-4))) > 1e6:
        #             pass
        #         else:
        #             pygame.draw.circle(screen, WHITE, (int(balls_reverse4[i][0]*(5-t) + balls_reverse5[i][0]*(t-4)),int(balls_reverse4[i][1]*(5-t) + balls_reverse5[i][1]*(t-4))),2)
        #     elif t>=5 and t<6:
        #         if abs(int(balls_reverse5[i][0]*(6-t) + balls_reverse6[i][0]*(t-5))) > 1e6:
        #             pass
        #         else:
        #             pygame.draw.circle(screen, WHITE, (int(balls_reverse5[i][0]*(6-t) + balls_reverse6[i][0]*(t-5)),int(balls_reverse5[i][1]*(6-t) + balls_reverse6[i][1]*(t-5))),2)
        #     elif t>=6 and t<7:
        #         if abs(int(balls_reverse6[i][0]*(7-t) + balls_reverse7[i][0]*(t-6))) > 1e6:
        #             pass
        #         else:
        #             # print("Os valores do erro sao: "+str(int(balls_reverse6[i][0]*(7-t) + balls_reverse7[i][0]*(t-6)))+" ou "+str(int(balls_reverse6[i][1]*(7-t) + balls_reverse7[i][1]*(t-6)))+"\n")
        #             pygame.draw.circle(screen, WHITE, (int(balls_reverse6[i][0]*(7-t) + balls_reverse7[i][0]*(t-6)),int(balls_reverse6[i][1]*(7-t) + balls_reverse7[i][1]*(t-6))),3)
        #     elif t>=7 and t<8:
        #         if abs(int(balls_reverse6[i][0]*(7-t) + balls_reverse7[i][0]*(t-6))) > 1e6:
        #             pass
        #         else:
        #             pygame.draw.circle(screen, WHITE, (int(balls_reverse7[i][0]*(8-t) + balls_reverse8[i][0]*(t-7)),int(balls_reverse7[i][1]*(8-t) + balls_reverse8[i][1]*(t-7))),2)
    
    # pygame.draw.circle(screen, WHITE, (int(balls_reverse[-1][0]*(2-t) + balls_reverse2[-1][0]*(t-1)),int(balls_reverse[-1][1]*(2-t) + balls_reverse2[-1][1]*(t-1))),3)
    clock.tick(360)
    pygame.display.update()