#!/usr/bin/env python3

import math

mass = 6000
density = 3000 # kg/m3

# Considering a square sat
volume = mass / density
side = volume ** (1./3.)

radius = (1./2.) * side * math.sqrt(3)

print("17) Volume, side, radius :", [volume, side, radius])


