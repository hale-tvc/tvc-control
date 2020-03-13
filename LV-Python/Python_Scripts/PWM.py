from PyDAQmx.DAQmxFunctions import *
from PyDAQmx.DAQmxConstants import *
import numpy as np

class ContinuousPulseTrainGeneration():
    """ Class to create a continuous pulse train on a counter

    Usage:  pulse = ContinuousTrainGeneration(period [s],
                duty_cycle (default = 0.5), counter (default = "dev1/ctr0"),
                reset = True/False)
            pulse.start()
            pulse.stop()
            pulse.clear()
    """
    def __init__(self, period, duty_cycle, counter, reset=None):
        self.period = period
        self.duty_cycle=duty_cycle
        self.counter=counter
        self.reset=reset

        if reset is None:
            self.reset = False
        if reset:
            DAQmxResetDevice(self.counter.split('/')[0])

        taskHandle = TaskHandle(0)
        DAQmxCreateTask("",byref(taskHandle))
        DAQmxCreateCOPulseChanFreq(taskHandle,self.counter,"",DAQmx_Val_Hz,DAQmx_Val_Low,
                                                                   0.0,1/float(self.period),self.duty_cycle)
        DAQmxCfgImplicitTiming(taskHandle,DAQmx_Val_ContSamps,1000)
        self.taskHandle = taskHandle
    def start(self):
        DAQmxStartTask(self.taskHandle)
    def stop(self):
        DAQmxStopTask(self.taskHandle)
    def clear(self):
        DAQmxClearTask(self.taskHandle)


if __name__=="__main__":
    pulse_gene1 = ContinuousPulseTrainGeneration(1.,0.5, "Dev1/ao0", reset=True)
    pulse_gene1.start()
    a = raw_input("Generating pulse train. Press Enter to interrupt\n")
    pulse_gene1.stop()
    pulse_gene1.clear()
