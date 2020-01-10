import numpy as np
import matplotlib.pyplot as plt 

class EMA:

    def __init__(self,mass,spring_constant,dampening,dt):
        self.m = mass # Kilograms
        self.k = spring_constant # Newtons per metre
        self.b = dampening 
        self.dt = dt # Seconds
    

    def acceleration(self,t):
        pass
    def velocity(self,state,t):
        pass

    def position(self,state,t,w):
    

        A1 = 1/((self.m/self.dt**2) + (self.b/self.dt) + (self.k))
        A2 = (-2*self.m/self.dt**2) - (self.b/self.dt)
        A3 = (self.m/self.dt**2) 
        
        x = np.zeros(len(t))


        #unpack state vector
        x[0],x[1]= state 
        
        for i in range(2,len(x)):
            x[i] = (A1)*(-A2*x[i-1] - A3*x[i-2]) + np.sin(w*t[i])

        return x
        

   
m = 100 #Kilogram
k = 20 #Newtons per metre
b = 30 
dt = 0.1
freq = 5 #Hz

w = 2*np.pi*freq

EMA = EMA(m,k,b,dt)

state = [10, 9]

t = np.arange(0.0, 60.0, dt)

pos = EMA.position(state,t,w)

plt.plot(t, pos)
plt.xlabel('TIME (sec)')
plt.ylabel('STATES')
plt.title('Mass-Spring System')
plt.legend(('$x$ (m)', '$\dot{x}$ (m/sec)'))
plt.show()
