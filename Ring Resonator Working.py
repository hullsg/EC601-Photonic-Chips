#Simulates circuit consisting of grating coupler recieving input light that is propogated through a ring resonator

import matplotlib.pyplot as plt
from simphony.libraries import siepic
from simphony.simulators import SweepSimulator

#establishing grating coupler to recieve input
gc_input = siepic.GratingCoupler()

#establishing waveguide between coupler and ring resonator
wg_1 = siepic.Waveguide()


#establishing first half-ring (gap = 30 nm, r = 10 microns)
halfring1 = siepic.HalfRing(radius = 1e-5)
#halfring1 = siepic.HalfRing(radius = 2e-5)
#halfring1 = siepic.HalfRing(radius=3e-5)

#establing second half-ring (gap = 30 nm, r = 10 microns)
halfring2 = siepic.HalfRing(radius=1e-5)
#halfring2 = siepic.HalfRing(radius=2e-5)
#halfring2 = siepic.HalfRing(radius=3e-5)

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
wg_1.connect(halfring1["in"])  #was "pass"

simulator = SweepSimulator(1.90e14, 1.957e14)  #frequency range in Hz, based on laser being 1.957e14 Hz
simulator.multiconnect(gc_input, halfring2["out"]) #was "out"

f, p = simulator.simulate()
plt.plot(f, p)
plt.title("Ring Resonator")
plt.xlabel("Frequencies")
plt.ylabel("Fractional Optical Power")
plt.tight_layout()
plt.show()
