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

#establishing y-branches from waveguides
ybranch1 = siepic.Ybranch(thickness = 220e-9)
ybranch2 = siepic.Ybranch(thickness = 220e-9)
ybranch3 = siepic.Ybranch(thickness = 220e-9)
ybranch4 = siepic.Ybranch(thickness = 220e-9)

#connecting waveguides to y-branches input
coupl_guide1['pin2'].connect(ybranch1['pin1'])
coupl_guide2['pin2'].connect(ybranch2['pin1'])
coupl_guide3['pin2'].connect(ybranch3['pin1'])
coupl_guide4['pin2'].connect(ybranch4['pin1'])

#establishing terminators
term1 = siepic.Terminator(w1=5e-07,w2=6e-08,L=1e-05)
term2 = siepic.Terminator(w1=5e-07,w2=6e-08,L=1e-05)
term3 = siepic.Terminator(w1=5e-07,w2=6e-08,L=1e-05)
term4 = siepic.Terminator(w1=5e-07,w2=6e-08,L=1e-05)

#connecting terminator to one output branch of y-branch
term1['pin1'].connect(ybranch1['pin2'])
term2['pin1'].connect(ybranch2['pin2'])
term3['pin1'].connect(ybranch3['pin2'])
term4['pin1'].connect(ybranch4['pin2'])

#establishing waveguides receiving input from y-branch
branch_guide1 = siepic.Waveguide(length = 200e-6)
branch_guide2 = siepic.Waveguide(length = 200e-6)
branch_guide3 = siepic.Waveguide(length = 200e-6)
branch_guide4 = siepic.Waveguide(length = 200e-6)

#connecting branch guides to second output of y-branch
branch_guide1['pin1'].connect(ybranch1['pin3'])
branch_guide2['pin1'].connect(ybranch2['pin3'])
branch_guide3['pin1'].connect(ybranch3['pin3'])
branch_guide4['pin1'].connect(ybranch4['pin3'])

#establishing y-branches from waveguides
combobranch1 = siepic.Ybranch(thickness = 220e-9)
combobranch2 = siepic.Ybranch(thickness = 220e-9)

#combining 2 branch guides to each input of y-branch
branch_guide1['pin2'].connect(combobranch1['pin2'])
branch_guide2['pin2'].connect(combobranch1['pin3'])
branch_guide3['pin2'].connect(combobranch2['pin2'])
branch_guide4['pin2'].connect(combobranch2['pin3'])

#final y-branch to combine everything into 1 output
outbranch = siepic.Ybranch(thickness = 220e-9)

#combining everything in to the outbranch
combobranch1['pin1'].connect(outbranch['pin2'])
combobranch2['pin1'].connect(outbranch['pin3'])
