import PyDAQmx as pd
import numpy as np

Pinout =  "Dev1/a01"

ini_delay = 0 # sec
frequency = 50  # Hz
duty_cycle = 0.05
task = pd.Task()
task.CreateCOPulseChanFreq(Pinout,  "CamTrigger",  pd.DAQmx_Val_Hz,  pd.DAQmx_Val_Low,   ini_delay,  frequency,  duty_cycle)
task.CfgImplicitTiming(pd.DAQmx_Val_ContSamps,  1000)



task.StartTask()

task.StopTask()
task.ClearTask()
