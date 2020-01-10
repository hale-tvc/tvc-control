import numpy as np 
import matplotlib.pyplot as plt 

class EMA(object):

    def __init__(self,mass,spring_constant,friction_constant):
        self.m = mass
        self.k = spring_constant 
        self.b = friction_constant 


