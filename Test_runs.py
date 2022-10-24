# run test trials for simphony

from simphony.libraries import siepic

component1 = siepic.Waveguide(length=500e-9)
component2 = siepic.Waveguide(length=1500e-9)
component1.connect(component2)
component1['pin2'].connect(component2['pin1'])
component1.rename_pins('input', 'output')
component1['output'].connect(component2)

from simphony.simulators import SweepSimulator
simulation = SweepSimulator(1500e-9, 1600e-9)
simulation.multiconnect(component1['input'],component2['pin2'])
result = simulation.simulate()


