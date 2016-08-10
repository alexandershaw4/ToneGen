#! /usr/bin/env python
# Harmonic sinusoidal tone generator
# for a c#: 270 540 810 1080 1350 1620 1890
# AS2016

import scipy.io as sio
import matplotlib as mp
import numpy as np
import os
import scipy.io.wavfile
import sys

inp      = sys.argv[1:]
freq     = np.array([int(l) for l in inp])

amp      = 10                           # amplitude 
fs       = 20500                        # sample freq
duration = 1                            # len in seconds
#freq    = np.array([500, 1000, 1500])  # frequencies
val      = np.arange(0,duration,1/fs)   # vector

# tone engine
def f(t):
    return amp*np.sin(2*np.pi*t*val)

# add sin waves
a = np.array([0 for x in range(val.shape[0])])
for i in freq:
    o = f(i)
    a = a + o

sio.wavfile.write('tone.wav',fs,a)
