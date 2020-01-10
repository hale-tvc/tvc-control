import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class EMA:

    def __init__(self,mass,spring_constant):
        self.m = mass # Kilograms
        self.k = spring_constant # Newtons per metre

    def MassSpring(self,state,t):
      # unpack the state vector
      x = state[0]
      xd = state[1]

      # these are our constants
      g = 9.8 # metres per second

      # compute acceleration xdd
      xdd = ((self.k*x)/self.m) + g

      # return the two state derivatives
      return [xd, xdd]


m = 1.5 #Kilogram
k = -2.5 #Newtons per metre

EMA = EMA(m,k)

state0 = [0.0, 0.0]
t = np.arange(0.0, 10.0, 0.1)

state = odeint(EMA.MassSpring, state0, t)

plt.plot(t, state)
plt.xlabel('TIME (sec)')
plt.ylabel('STATES')
plt.title('Mass-Spring System')
plt.legend(('$x$ (m)', '$\dot{x}$ (m/sec)'))

plt.show()
