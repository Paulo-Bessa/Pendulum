import numpy as np

# Define as constantes do sistema de Lorenz
sigma = 10
rho = 28
beta = 8/3

# Define a função que descreve o sistema de Lorenz
def lorenz(x, y, z):
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return dx_dt, dy_dt, dz_dt

# Define a função que calcula o vetor tangente a uma órbita
def tangent_vector(x, y, z, v):
    dx_dt, dy_dt, dz_dt = lorenz(x, y, z)
    return np.array([dx_dt, dy_dt, dz_dt]) @ v

# Define a função que normaliza um vetor
def normalize(v):
    return v / np.linalg.norm(v)

# Define as condições iniciais e o vetor tangente inicial
x0 = np.array([1, 1, 1])
v0 = np.array([0, 1, 0])

# Normaliza o vetor tangente inicial
v0 = normalize(v0)

# Define o número de iterações e o tamanho do passo
n_iter = 10000
dt = 0.01

# Inicializa as variáveis para o cálculo do expoente de Lyapunov
v = np.zeros((3, 3))
v[0] = v0
d = np.zeros(3)
d[0] = np.linalg.norm(v0)

# Realiza as iterações e calcula o maior expoente de Lyapunov
for i in range(n_iter):
    x, y, z = x0 + v[0] * d[0]
    t = tangent_vector(x, y, z, v[0])
    for j in range(1, 3):
        t -= np.dot(t, v[j-1]) * v[j-1]
        if np.linalg.norm(t) == 0:
            t = np.random.rand(3)
        v[j] = normalize(t)
        d[j] = tangent_vector(x, y, z, v[j])
    d = d / np.linalg.norm(d)
    if np.any(np.isinf(np.log(d))) or np.any(np.isnan(np.log(d))):
        lyap = 0
        break
    lyap = np.sum(np.log(d)) / (i*dt)
    
print("O maior expoente de Lyapunov é:", lyap)
