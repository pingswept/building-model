from math import pi, atanh
lam = 2.8 # soil conductivity, W/(m*K)
B = 13.4 # breadth in m (44 ft)
W = 0.2 # wall thickness in m
L = 22.25 # length in m (73 ft)
U = ((4*lam)/(pi*B)) * atanh(B/(B+W)) # Macey's model, without length correction
print(U)
Tin = 33.0 # floor temp in deg. C
Tout = 0.0 # winter!
Q = (Tin - Tout)*U*B*L
print("Power lost to slab: {0} [W]".format(Q))
price_per_kWh = 0.20 # $/kWh
hourly_cost = Q*price_per_kWh/1000.0
print(hourly_cost)
