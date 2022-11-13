import matplotlib.pyplot as plt
from simphony.libraries import siepic
from simphony.simulation import Detector, Laser, Simulation

#establishing grating coupler
coupler1 = siepic.GratingCoupler(thickness = 220e-9, deltaw = 0, polarization = "TE")  

#establishing waveguide receiving input from grating couplers
coupl_guide1 = siepic.Waveguide(length = 200e-6)

#connecting coupler to waveguide
coupler1['pin1'].connect(coupl_guide1['pin1'])

#establishing first half-ring (gap = 30 nm, r = 10 microns)
halfa_1 = siepic.HalfRing()

#establing second half-ring (gap = 30 nm, r = 10 microns)
#halfb_1 = siepic.HalfRing()

#connecting two halves of each half-ring
#halfa_1['pin1'].connect(halfb_1['pin1'])
#halfa_1['pin3'].connect(halfb_1['pin3'])

#connecting coupl_guide to ring resonator
coupl_guide1['pin2'].connect(halfa_1['pin2'])

theoretical = None
with Simulation() as sim:
    l=Laser(power=20e-3)
    l.wlsweep(1500-9, 1600-9)
    l.connect(coupler1)
    Detector().connect(halfa_1)

    theoretical = sim.sample()

plt.plot(sim.freqs, theoretical[:, 0, 0])
plt.title("Attentuator")
plt.tight_layout()
plt.show()
