from Lyapunov.runge_kutta import *
from poincare import poincare_section
from duffing import duf_osc, Jacobian_duf, DF_Dparameter
from OPI import identify_UPO,modulo_UPO,distance
import matplotlib.pyplot as plt
import numpy as np
from csv import reader


def control_sc():
    print("Começou")
    # Parameters od Duffing Oscilator
    ALPHA=0.05
    GAMMA=-0.2
    BETA=1
    OMEGA=1
    MU=7.5
    PERIOD2= 3

    position=[]
    velocity=[]
    time=[]

    tmax = 2000
    t0 = 0
    step = 1e-3
    init = np.array([1,1])
    eps = 0
    tol = 2e-3
    rad_trap = 5e-2

    print("Importando dados.")
    with open('NOVO1.csv', 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            # row variable is a list that represents a row in csv
            position.append(float(row[0]))
            velocity.append(float(row[1]))
            time.append(float(row[2]))
    print("Dados importados.")
    print("Criando as seções de Poincaré")
    # Creation of Poincare sections
    ans = [position,velocity]
    sections = []
    for freq in np.linspace(0,2*np.pi,16):
        section = poincare_section(ans,time,OMEGA,eps=freq)
        sections.append(section)

    print("Seções de Poincaré criadas.")
    print("Identificando UPOs")
    # Identification of UPOs
    prox2 = identify_UPO(sections[0],PERIOD2,tol=rad_trap)
    proximities2 = modulo_UPO(prox2,sections[0],tol=rad_trap*3)
    print("UPOs identificadas. A primeira eh: "+str(proximities2[0]))

    # First UPO identified
    NUM=prox2[4]
    mu=MU

    # UPO in the Poincare sections
    sections_UPO = [elem[NUM] for elem in sections]
    print("Começando o controle")
    valores=[]
    tempos=[]
    while t0<=tmax:
        if eps>=len(sections_UPO):
            eps=0
        # System simulation
        # print("Simulando o sistema")
        valores.append(init)
        tempos.append(t0)
        FUNC = lambda x,t:duf_osc(x,t,mu=MU)
        init,t0 = rk4_step(FUNC,init,t0,h=step)
        # Creating the Poincaré section
        # if (t0+eps)%(2*np.pi*OMEGA)<1e-2:
        # Verification if the system get's into the attraction basin
        # print("Distancia eh de: "+str(distance(init,sections_UPO[eps])))
        if distance(init,sections_UPO[eps])<rad_trap:
            print("Entrou na bacia de atração")
            J = Jacobian_duf(init,t0)
            Wn = DF_Dparameter(init,t0)
            print("Valor de eps eh: "+str(eps))
            print("O valor limite que pode assumir eh: "+str(len(sections_UPO)))
            delta_state = init - sections_UPO[eps]
            dP = -np.array([[MU-mu]])

            S,V,D = np.linalg.svd(J)
            st_dir = D.T[0]
            # print("Shape de dir eh "+str(np.shape(st_dir))+" e o shape do Wn eh "+str(np.shape(Wn)))
            pre_res = np.array([[st_dir],[Wn]])
            res = np.linalg.pinv(pre_res)
            numi=J@delta_state@res
            # print("O vetor [alpha, -dp] eh: "+str(numi))
            # MU+=numi[0][0]
            rho=0
            downy=(st_dir@Wn)
            print("Downy: "+str(downy))
            uppy=(st_dir@delta_state)
            print("Uppy: "+str(uppy))
            MU += (1-rho-V[0])*uppy/downy
            # next = J@delta_state + Wn@dP
            eps+=1
    valores=np.array(valores)
    PRE=800000
    POS=-1
    plt.plot(valores.T[0][PRE:POS],valores.T[1][PRE:POS],linewidth=.1)
    plt.xlabel("Posição")
    plt.ylabel("Velocidade")
    # fig,ax=plt.subplots(ncols=2,nrows=2)
    # ax[0][0].plot(tempos[PRE:POS],valores.T[0][PRE:POS],":",markersize=.1)
    # ax[0][1].plot(tempos[PRE:POS],valores.T[1][PRE:POS],":",markersize=.1)
    # ax[1][0].plot(valores.T[0][PRE:POS],valores.T[1][PRE:POS],linewidth=.1)
    # # ax[1][0].plot(sections_UPO[eps][0],sections_UPO[eps][1],"o",color="red")
    # ax[1][0].set_xlabel("Posição")
    # ax[1][0].set_ylabel("Velocidade")
    # ax[1][1].plot(position,velocity,linewidth=.1)
    # ax[1][1].set_xlabel("Posição")
    # ax[1][1].set_ylabel("Velocidade")
    plt.show()
    return 0