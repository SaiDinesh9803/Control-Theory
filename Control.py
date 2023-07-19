import numpy as np
from scipy.integrate import odeint

g = 9.8


# The following function gives the ordinary differential
# equation that our plant follows. Do not meddle with this.
def f(x, t, theta):
    return (x[1], (-5 * g / 7) * np.radians(theta))


# Write your function here.

def solve():

    dx = 0

    return dx
