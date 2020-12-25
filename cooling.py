#!/usr/bin/env python3

from warming import total_energy, geo_temperature, emissivity, absorbtivity

eta_ins = 0.4 
eq_power = 700 # watts
max_temp = 40 + 273.15 # kelvin
o = 5.67e-8

emitted_power = (eta_ins * total_energy) + eq_power
print("emitted power : ", emitted_power)

radiator_sfc = emitted_power / (o*emissivity*(max_temp**4))
print("radiator surface : ", radiator_sfc)

new_absorbtivity = 0.15
new_emissivity = 0.75

new_radiator_sfc = emitted_power / (o*new_emissivity*(max_temp**4))
print("new radiator surface : ", new_radiator_sfc)
