import pybamm
import numpy as np
import os
import matplotlib.pyplot as plt

os.chdir(pybamm.__path__[0] + '/..')

model = pybamm.lithium_ion.SPM()
variable = list(model.rhs.keys())[1]
equation = list(model.rhs.values())[1]
print('rhs equation for variable \'', variable, '\' is:')
path = 'examples/notebooks/models/'
equation.visualise(path + 'spm1.png')

