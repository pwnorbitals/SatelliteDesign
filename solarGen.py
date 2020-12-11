import numpy as np


eff_cell = 0.31
Kr = 0.89
Km = 0.89
C0 = 1353
Ka = 1.2 # donné dans corrigé page 6
density = 6.18

convert_factor = 1/(0.77)
Pgs, Pgsm, Pgsn = (1137.4590321958742, 1080.5860805860805, 1364.950838635049)

Asg = (Ka*Pgsm)/(Km * C0 * eff_cell)
print("Asg = ", round(Asg,2))

Asgp = Asg * convert_factor
print("Asgp = ", round(Asgp,2))

mass_panel = round(Asgp * density,2)
print("Mass panel in kg : ", mass_panel)



