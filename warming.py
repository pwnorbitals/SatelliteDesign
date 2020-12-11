#!/usr/bin/env python3

import math
import numpy as np

mass = 6000
density = 3000 # kg/m3

# Considering a square sat
volume = mass / density
side = volume ** (1./3.)

radius = (1./2.) * side * math.sqrt(3)

print("17) Volume, side, radius :", [volume, side, radius])



solar_cst = 1353
albedo_earth = 0.3
albedo_flux = 0.35 * solar_cst
terrestrial_flux = (1./4.) * (solar_cst - albedo_flux)
diameter = 2 * radius
proj_surface = math.pi * (radius**2)
surface = 4 * math.pi * (radius**2)
sun_absorbtivity = np.array([0.95, 0.15, 0.30])
emissivity = np.array([0.90, 0.85, 0.03])
solar_energy = sun_absorbtiity * proj_surface * solar_cst
albedo_energy = 0
terrestrial_energy =  0
total_energy = math.sum([solar_energy, albedo_energy, terrestrial_energy])
geo_temperature = (total_energy/(emissivity * 5.67e-8 * proj_surface))**(1./4.)