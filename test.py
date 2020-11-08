#!/usr/bin/env python
import numpy as np
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite
import dimod
import dwave.inspector

Q = {}

Q[(1, 1)] = 3
Q[(1, 2)] = -5
Q[(1, 3)] = 3
Q[(1, 4)] = -2
Q[(2, 2)] = -2
Q[(2, 4)] = 4
Q[(3, 3)] = -5
Q[(3, 4)] = 4
Q[(4, 4)] = -6

#Q = {(0, 0): 1, (1, 1): 2.0, (3, 3): 9.0, (2, 2): -1.0, (2, 3): 2.0, (0, 2): 3.0, (0, 1): -2.0, (1, 2): -2.0, (0, 3): -6.0, (1, 3): -6.0} 

chainstrength = 1
numruns = 10

# Run the QUBO on the solver from your config file
sampler = EmbeddingComposite(DWaveSampler())
response = sampler.sample_qubo(Q, chain_strength=chainstrength, num_reads=numruns, annealing_time=20)

dwave.inspector.show(response)

print(response)