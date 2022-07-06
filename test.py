import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
oznake = ['TIP', 'CLANOV', 'OTROK', 'DOHODEK', 'CETRT', 'IZOBRAZBA']
n = 100
kibergrad = pd.read_csv('naloga/Kibergrad.csv', names=oznake)
S_cetrt = list(map(int, list(kibergrad[kibergrad.CETRT == "1"].DOHODEK)))
V_cetrt = list(map(int, list(kibergrad[kibergrad.CETRT == "2"].DOHODEK)))
J_cetrt = list(map(int, list(kibergrad[kibergrad.CETRT == "3"].DOHODEK)))
Z_cetrt = list(map(int, list(kibergrad[kibergrad.CETRT == "4"].DOHODEK)))
dohodki = list(map(int, list(kibergrad.DOHODEK)[1:]))

celotna_var = np.var(dohodki)
celotna_pric = np.mean(dohodki)

Sp = np.mean(S_cetrt)
Vp = np.mean(V_cetrt)
Jp = np.mean(J_cetrt)
Zp = np.mean(Z_cetrt)

pric = [Sp,Vp, Jp, Zp]

Sv = np.var(S_cetrt)
Vv = np.var(V_cetrt)
Jv = np.var(J_cetrt)
Zv = np.var(Z_cetrt)

vari = [Sv,Vv,Jv,Zv]

N = 43886
Ni = [10149, 10390, 13457, 9890]
wi = [x/N for x in Ni]

poj = sum([wi[i]*(pric[i] - celotna_pric)**2 for i in range(4)])
poj2 = sum([wi[i]*pric[i]**2 for i in range(4)]) - celotna_pric**2
nepoj = sum([wi[i]*vari[i] for i in range(4)])

print(celotna_var)
print(poj)
print(nepoj)
print(poj + nepoj)

print("-----------------------")

