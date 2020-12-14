import numpy as np

Re = 6371e3
mu = 3.986004e14 # Note sure
g0 = 9.81

def getVelocity(a,r):
    # a and r in m
    # V in m/s
    V = np.sqrt(mu*(2/r - 1/a))
    return V

def getA(zp,za):
    a = Re + (zp+za)/2
    return a

def getMassProp(DeltaV, ISP, mi):
    mf = mi /(np.exp(DeltaV /(ISP * g0)))
    mp = mi - mf
    return mp

################################### Q1 & Q2 ############################################

mi = 6000

za_GEO = 35786e3
za_GTO = 35786e3
za_190 = 190e3

zp = 190e3
zp_GEO = 35786e3

ISP_LEO2GTO = 280
ISP_GTO2GEO = 300
ISP_chem = 290
ISP_elec = 1700

thrust_chem = 20 # Newtons
eff_chem = 1

thrust_elec = 0.09 # Newtons
eff_elec = 0.7

rp_GTO = zp + Re
ra_GTO = za_GTO + Re
rp_GEO = zp_GEO + Re

# compute V circular orbit 190km
a_190 = getA(zp,za_190)
print("a_190 in m : ", a_190)
V_circular_190km = getVelocity(a_190,rp_GTO)

# compute V GTO
a_GTO = getA(zp,za_GTO)
Vp_GTO = getVelocity(a_GTO,rp_GTO)
Va_GTO = getVelocity(a_GTO, ra_GTO)

deltaV_GTO = Vp_GTO - V_circular_190km
print("DeltaV LEO-GTO in m/s : ", round(Vp_GTO, 2), "-", round(V_circular_190km, 2), "=", round(deltaV_GTO,2))

mp = getMassProp(deltaV_GTO, ISP_LEO2GTO, mi)
print("MassProp needed in kg : ", round(mp,2))

mi_GTO2GEO = mi - mp

a_GEO = getA(zp_GEO, za_GEO)
V_GEO = getVelocity(a_GEO, rp_GEO)

deltaV_GEO = V_GEO - Va_GTO
print("\nDeltaV GTO-GEO in m/s : ", round(deltaV_GEO, 2))

mp_GTO2GEO = getMassProp(deltaV_GEO, ISP_GTO2GEO, mi_GTO2GEO)
print("MassProp needed in kg : ", round(mp_GTO2GEO,2))

################################## Q3 & Q4 #############################################

mi_GEO = mi_GTO2GEO - mp_GTO2GEO

ISP_chem = 290
ISP_elec = 1700

thrust_chem = 20 # Newtons
eff_chem = 1

thrust_elec = 0.09 # Newtons
eff_elec = 0.7

deltaV_drag = 55 * 17 # 55 m/s per year * 17 years

print("\nDeltaV GEO with drag in m/s : ", round(deltaV_drag,2))
mp_drag_chem = getMassProp(deltaV_drag,ISP_chem, mi_GEO)
mp_desorbit_chem = getMassProp(6, ISP_chem, mi_GEO - mp_drag_chem)
print("MassProp needed for drag comp. with chem. engine in kg : ", round(mp_drag_chem,2))
print("MassProp needed for desorbiting with chem. engine in kg : ", round(mp_desorbit_chem, 2))
print("Total mass prop. with chemical engine in kg : ", round(mp_drag_chem + mp_desorbit_chem,2))

mp_drag_elec = getMassProp(deltaV_drag, ISP_elec, mi_GEO)
mp_desorbit_elec = getMassProp(6, ISP_elec, mi_GEO - mp_drag_elec)
print("\nMassProp needed with elec. engine in kg : ", round(mp_drag_elec,2))
print("MassProp needed for desorbiting with elec. engine in kg : ", round(mp_desorbit_elec, 2))
print("Total mass prop. with elec engine in kg : ", round(mp_drag_elec + mp_desorbit_elec,2))

payload_mass_elec = mi_GEO - (mp_drag_elec + mp_desorbit_elec)
payload_mass_chem = mi_GEO - (mp_drag_chem + mp_desorbit_chem)
print("\nPayload mass with chem engine in kg : ", round(payload_mass_chem,2))
print("Payload mass with chem engine in kg : ", round(payload_mass_elec,2))

print("Mass diff in kg : ", round(payload_mass_elec-payload_mass_chem,2))