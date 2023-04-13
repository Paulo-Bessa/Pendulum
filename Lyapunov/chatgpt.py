# import numpy as np

# def lyapunov_exponent(f, x0, n, delta=1e-8):
#     """
#     Calculates the Lyapunov exponent of a given multi-variable function f.
    
#     Parameters:
#         f (function): the function to calculate the Lyapunov exponent for.
#         x0 (numpy array): the initial condition.
#         n (int): the number of iterations.
#         delta (float, optional): the perturbation to the initial condition.
    
#     Returns:
#         The Lyapunov exponent.
#     """
#     # Calculate the Jacobian of the function f
#     def jacobian(x):
#         h = delta
#         n = len(x)
#         J = np.zeros((n, n))
#         for i in range(n):
#             x_plus = x.copy()
#             x_plus[i] += h
#             x_minus = x.copy()
#             x_minus[i] -= h
#             J[:, i] = (f(x_plus) - f(x_minus)) / (2 * h)
#         return J
    
#     def lin_lorenz(x,sigma=16,R=45.92,b=4):
#         x11 = -sigma
#         x12 = sigma
#         x13 = 0
#         x21 = R-x[2]
#         x22 = -1
#         x23 = -x[0]
#         x31 = x[1]
#         x32 = x[0]
#         x33 = -b
#         return np.array([[x11,x12,x13],
#                         [x21,x22,x23],
#                         [x31,x32,x33]])
    
#     # Initialize the variables
#     x = x0
#     lyap_sum = 0
#     cont=0
#     # Iterate n times
#     for i in range(n):
#         print(cont)
#         cont+=1
#         # Calculate the Jacobian of the function at the current point
#         J = lin_lorenz(x)
#         print("O valor do jacobiano esta: "+str(J))
#         print("O valor do sistema esta: "+str(x))
#         # Calculate the singular values of the Jacobian using SVD
#         U, S, V = np.linalg.svd(J)
        
#         # Calculate the norm of the singular values
#         norm_s = np.sqrt(np.sum(S**2))
        
#         # Update the sum of the Lyapunov exponents
#         lyap_sum += np.log(norm_s)
        
#         # Update the current point
#         x = f(x)
    
#     # Calculate the Lyapunov exponent as the average of the sum
#     lyap_exp = lyap_sum / n
    
#     return lyap_exp

# # Define the logistic map function
# def logistic_map(x, r):
#     return r * x * (1 - x)

# # Define the Lorenz System
# def lorenz(x,y,z,t,sigma,rho,beta):
#     x1 = sigma*(y-x)
#     x2 = x*(rho-z)-y
#     x3 = x*y-beta*z
#     return np.array([x1,x2,x3])

# # Define the multi-variable Henon map function
# def henon_map(x, y, a, b):
#     x_new = 1 - a * x**2 + y
#     y_new = b * x
#     return np.array([x_new, y_new])

# # Calculate the Lyapunov exponent for the Henon map function
# lyap_exp = lyapunov_exponent(lambda x: lorenz(x[0], x[1], x[2], 0, 16, 45.92, 4), np.array([1, 1, 1]), 1000)
# print("Lyapunov exponent:", lyap_exp)


import numpy as np

def lyapunov_exponent(f, J, x0, n, delta=1e-8):
    """
    Calculates the Lyapunov exponent of a given multi-variable dynamical system.
    
    Parameters:
        f (function): the function that defines the dynamical system.
        J (function): the function that computes the Jacobian matrix of f.
        x0 (numpy array): the initial condition.
        n (int): the number of iterations.
        delta (float, optional): the perturbation to the initial condition.
    
    Returns:
        The Lyapunov exponent.
    """
    # Initialize the variables
    x = x0
    lyap_sum = 0
    
    # Iterate n times
    for i in range(n):
        # Calculate the Jacobian of the function at the current point
        J_x = J(x)
        
        # Calculate the singular values of the Jacobian using SVD
        U, S, V = np.linalg.svd(J_x)
        
        # Calculate the norm of the singular values
        norm_s = np.sqrt(np.sum(S**2))
        
        # Update the sum of the Lyapunov exponents
        lyap_sum += np.log(norm_s)
        
        # Update the current point
        x = f(x)
        
        # Perturb the current point
        dx = np.random.rand(*x.shape) * delta
        x += dx
        
    # Calculate the Lyapunov exponent as the average of the sum
    lyap_exp = lyap_sum / n
    
    return lyap_exp

# Define the Lorenz system of differential equations
def lorenz_system(x, y, z, s, r, b):
    dx_dt = s * (y - x)
    dy_dt = r * x - y - x * z
    dz_dt = x * y - b * z
    return np.array([dx_dt, dy_dt, dz_dt])

# Define the Jacobian matrix of the Lorenz system
def jacobian_lorenz(x, y, z, s, r, b):
    J = np.array([
        [-s, s, 0],
        [r - z, -1, -x],
        [y, x, -b]
    ])
    return J

# Calculate the Lyapunov exponent for the Lorenz system
lyap_exp = lyapunov_exponent(lambda x: lorenz_system(x[0], x[1], x[2], 10, 28, 8/3), lambda x: jacobian_lorenz(x[0], x[1], x[2], 10, 28, 8/3), np.array([1, 1, 1]), 10000)
print("Lyapunov exponent:", lyap_exp)
