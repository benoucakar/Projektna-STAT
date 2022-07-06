import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
oznake = ['TIP', 'CLANOV', 'OTROK', 'DOHODEK', 'CETRT', 'IZOBRAZBA']
n = 100
kibergrad = pd.read_csv('naloga/Kibergrad.csv', names=oznake)
# S, V, J, Z
cetrti = [kibergrad[kibergrad.CETRT == str(i)] for i in range(1,5)]

seed = 2
vzorci = [list(map(int, list(cetrti[i].sample(n, replace=False, random_state=seed).DOHODEK))) for i in range(4)]


N = 43886
Ni = [10149, 10390, 13457, 9890]
wi = [x/N for x in Ni]

povpi = [np.mean(vzorci[i]) for i in range(4)]
Si = [n * np.var(vzorci[i]) for i in range(4)]
skupno_povp = sum(povpi) / 4

nepoj_cen = sum([wi[i]*(Ni[i]-1) / Ni[i] * Si[i] / (n-1) for i in range(4)])
poj_cen = sum([wi[i]*((povpi[i]-skupno_povp)**2 - ((1-wi[i])*(Ni[i]-n)*Si[i])/(Ni[i]*n*(n-1))) for i in range(4)]) 

print(poj_cen)
print(nepoj_cen)
print(poj_cen+nepoj_cen)

#9434624.656322591
#901180942.5834997
#910615567.2398223