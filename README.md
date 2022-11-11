 EC601-Photonic-Chips
I am using the photonic integrated circuit simulator Simphony to construct components and circuits of photonic chips.  The simulator is being used under open source MIT License.

A conda environment was created for the Anaconda Python distribution using conda create -n Photon_test python=3.9.12 anaconda.  The environment is activated using conda activate Photon_test.

Simphony was installed into the environment using pip install simphony.

Citation: S. Ploeg, H. Gunther and R. M. Camacho, “Simphony: An Open-Source Photonic Integrated Circuit Simulation Framework,” in Computing in Science & Engineering, vol. 23, no. 1, pp. 65-74, 1 Jan.-Feb. 2021, doi: 10.1109/MCSE.2020.3012099

To represent a single neuron, an input pixel array is represented grating couplers (in this case, 4 couplers in a 2 x 2 array).  The grating couplers are connected via waveguide to either a y-branch branching into a terminator and a second waveguide, or a half-ring resonator (both in replacement of an optical attentuator).  The outputs of these components are combined into a singular output using a series of y-branches.  
