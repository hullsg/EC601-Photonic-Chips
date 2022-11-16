#Simulates a circuit consisting of  grating coupler receiving input light that propogates through a ring resonator

import matplotlib.pyplot as plt
from simphony.libraries import siepic
from simphony.simulators import SweepSimulator

gc_input = siepic.GratingCoupler()

#establishing waveguide between coupler and ring resonator
wg_1 = siepic.Waveguide()


#establishing first half-ring (gap = 30 nm, r = 10 microns)
halfring1 = siepic.HalfRing()

#establing second half-ring (gap = 30 nm, r = 10 microns)
halfring2 = siepic.HalfRing()

#establishing terminator to remove back-scattering effects
terminator = siepic.Terminator()

#renaming pins of each half-ring
halfring1.rename_pins("pass", "midb", "in", "midt")
halfring2.rename_pins("out", "midt", "term", "midb")

#connects the two half-rings to make a complete ring
#connects terminator to output of ring resonator
halfring1.interface(halfring2)
halfring2["term"].connect(terminator)

#connecting grating coupler to waveguide
wg_1.connect(gc_input["pin1"])
#connecting ring to waveguide
wg_1.connect(halfring1["pass"])

simulator = SweepSimulator(1500e-9, 1600e-9)
simulator.multiconnect(gc_input, halfring2["out"])

f, p = simulator.simulate()
plt.plot(f, p)
plt.title("Ring Resonator")
plt.xlabel("Frequencies")
plt.ylabel("Fractional Optical Power")
plt.tight_layout()
plt.show()
