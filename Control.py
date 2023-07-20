import numpy as np
from scipy.integrate import odeint

g = 9.8

y0 = [0, 0]
tf = 1000
n = 1001
t = np.linspace(0, tf, n)


# The following function gives the ordinary differential
# equation that our plant follows. Do not meddle with this.
def f(x, t, theta):
    return (x[1], (-5 * g / 7) * np.radians(theta))


# Write your function here.

def solve(theta):
    for i in range(1, len(t)):
        ts = [t[i-1], t[i]]
        dx = odeint(f, y0, ts, args=(theta, ))

    return dx

def PIDLoop(x , sp_x):
    k_p = 0.5
    # k_i = 1
    # k_d = 0.2
    
        
    e = x - sp_x
    
    act = k_p * e
    
    theta = act
        
    return theta
        