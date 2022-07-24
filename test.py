import pybamm

# Choose the Model
model = pybamm.lithium_ion.DFN()

sim = pybamm.Simulation(model)
sim.solve(t_eval=[0, 3600])
sim.plot()
