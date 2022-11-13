from simphony.libraries import siepic

#establishing grating couplers (assume 2x2 pixel array)
coupler1 = siepic.GratingCoupler(thickness = 220e-9, deltaw = 0, polarization = "TE")  
coupler2 = siepic.GratingCoupler(thickness = 220e-9, deltaw = 0, polarization = "TE")  
coupler3 = siepic.GratingCoupler(thickness = 220e-9, deltaw = 0, polarization = "TE")  
coupler4 = siepic.GratingCoupler(thickness = 220e-9, deltaw = 0, polarization = "TE")  


#establishing waveguides receiving input from grating couplers
coupl_guide1 = siepic.Waveguide(length = 200e-6)
coupl_guide2 = siepic.Waveguide(length = 200e-6)
coupl_guide3 = siepic.Waveguide(length = 200e-6)
coupl_guide4 = siepic.Waveguide(length = 200e-6)

#connecting couplers to waveguides
coupler1['pin1'].connect(coupl_guide1['pin1'])
coupler2['pin1'].connect(coupl_guide2['pin1'])
coupler3['pin1'].connect(coupl_guide3['pin1'])
coupler4['pin1'].connect(coupl_guide4['pin1'])

#establishing first half-ring (gap = 30 nm, r = 10 microns)
halfa_1 = siepic.HalfRing()
halfa_2 = siepic.HalfRing()
halfa_3 = siepic.HalfRing()
halfa_4 = siepic.HalfRing()

#establing second half-ring (gap = 30 nm, r = 10 microns)
halfb_1 = siepic.HalfRing()
halfb_2 = siepic.HalfRing()
halfb_3 = siepic.HalfRing()
halfb_4 = siepic.HalfRing()

#connecting two halves of each corresponding half-ring
halfa_1['port1'].connect(halfb_1['port1'])
halfa_1['port3'].connect(halfb_1['port3'])
halfa_2['port1'].connect(halfb_2['port1'])
halfa_2['port3'].connect(halfb_2['port3'])
halfa_3['port1'].connect(halfb_3['port1'])
halfa_3['port3'].connect(halfb_3['port3'])
halfa_4['port1'].connect(halfb_4['port1'])
halfa_4['port3'].connect(halfb_4['port3'])

#connecting coupl_guides to ring resonators
coupl_guide1['pin2'].connect(halfa_1['port2'])
coupl_guide2['pin2'].connect(halfa_2['port2'])
coupl_guide3['pin2'].connect(halfa_3['port2'])
coupl_guide4['pin2'].connect(halfa_4['port2'])


