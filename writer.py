import csv
import numpy as np

# define o nome do arquivo e o cabeçalho
filename = "Dados_pendulo.csv"
header = ["Time", "Position", "Velocity"]

# define os dados que você deseja escrever no arquivo
dados = [
    ["João", 25, "São Paulo"],
    ["Maria", 30, "Rio de Janeiro"],
    ["Pedro", 20, "Belo Horizonte"]
]

zeta = 2.368e-5 #kgm^2/s
I  = 1.738e-4 #kgm^2
k  = 2.47 #N/m
d  = 4.8e-2 #m
D  = 9.5e-2 #m
mu = 1.272e-4 #Nm
m  = 1.47e-2 #kg
g  = 9.81 #m/s^2
a  = 1.6e-1 #m 
b  = 6.0e-2 #m
q  = 1e6
omega = 5.61
params = [zeta,I,k,d,D,mu,m,g,a,b,q,omega]

omega=np.pi
def mode(x,t):
    zeta=params[0]
    I=params[1]
    k=params[2]
    d=params[3]
    D=params[4]
    mu=params[5]
    m=params[6]
    g=params[7]
    a=params[8]
    b=params[9]
    q=params[10]
    omega=params[11]
    K = (2/np.pi)*mu*np.atan(q*x[2])
    
    one=x[2]
    two=(k*d/(2*I))*(np.sqrt(a^2+b^2-2*a*b*np.cos(omega))-(a-b))-(zeta/I)*x[2]-(k*(d^2)/(2*I))*x[1]-K/I-(m*g*D*np.sin(x[1])/(2*I))
#     three = omega
    return np.array([one,two])#,three)

# abre o arquivo em modo de escrita e define o separador como vírgula
with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file, delimiter=",")
    
    # escreve o cabeçalho
    writer.writerow(header)
    
    # escreve os dados
    writer.writerows(dados)