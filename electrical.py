#!/usr/bin/env python3

T = 86142/(60*60)              # orbital period, seconds to change
Psl = 1e3 
Pslt = 2e3
Tt = 24*60*60
nreg = 0.93
nbat = 0.91
Tt_avg = 0.05* T    # Eclipse time per period, seconds

Te = Tt_avg # Eclipse time, seconds
Td = T - Te # Day time, seconds
Ka = 1.2    # GEO form factor

Pgs = (Psl/nreg) * (1 + ((Te/Td)/nbat))
Pgsm = Pgs * (Td/T)
Pgsn = Ka * Pgs

print("Pgs, Pgsm, Pgsn : ", [Pgs, Pgsm, Pgsn])

DOD1 = 0.8
DOD_init = 0.3
DOD2 = 0.7

Wbat1 = (Pslt*Tt) / (DOD1 - DOD_init)
Wbat2 = (Psl*Te) / DOD2
Wbat = max([Wbat1, Wbat2])
Mbat = 10 * Wbat # 10 kg / kWh

print("Wbat1, Wbat2, Wbat, Mbat :", [Wbat1, Wbat2, Wbat, Mbat])