#!/usr/bin/env python3

T = 7200              # orbital period, seconds to change
Psl = 1e3 
Pslt = 2e3
Tt_s = 24*60*60
nreg = 0.93
nbat = 0.91
Tt_avg = 0.05* T_s    # Eclipse time per period, seconds

Te = Tt_avg # Eclipse time, seconds
Td = T - Te # Day time, seconds
Ka = 1.2    # GEO form factor

Pgs = (Psl/nreg) * (1 + ((Te/Td)/nbat))
Pgsm = Pgs * (Td/T)
Pgsn = Ka * Pgs

DOD1 = 0.8
DOD_init = 0.3
DOD2 = 0.7

Wbat1 = (Pslt*Tt) / (DOD1 - DOD_init)
Wbat2 = (Psl*Te) / DOD2
Wbat = math.max([Wbat1, Wbat2])
Mbat = 10 * Wbat # #0 kg / kWh