import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
oznake = ['TIP', 'CLANOV', 'OTROK', 'DOHODEK', 'CETRT', 'IZOBRAZBA']
n = 100
kibergrad = pd.read_csv('naloga/Kibergrad.csv', names=oznake)
S_cetrt = kibergrad[kibergrad.CETRT == "1"]
V_cetrt = kibergrad[kibergrad.CETRT == "2"]
J_cetrt = kibergrad[kibergrad.CETRT == "3"]
Z_cetrt = kibergrad[kibergrad.CETRT == "4"]
    
# ----------------- (a) naloga ----------------- #

seed = 2
enst_vrzc_S_dohodek = list(map(int, list(S_cetrt.sample(n, replace=False, random_state=seed).DOHODEK)))
enst_vrzc_V_dohodek = list(map(int,list(V_cetrt.sample(n, replace=False, random_state=seed).DOHODEK)))
enst_vrzc_J_dohodek = list(map(int,list(J_cetrt.sample(n, replace=False, random_state=seed).DOHODEK)))
enst_vrzc_Z_dohodek = list(map(int,list(Z_cetrt.sample(n, replace=False, random_state=seed).DOHODEK)))

vzorci1 = [enst_vrzc_S_dohodek, enst_vrzc_V_dohodek, enst_vrzc_J_dohodek, enst_vrzc_Z_dohodek]

fig = plt.figure(figsize =(8, 6))
ax1 = fig.add_subplot(111)
bp1 = ax1.boxplot(vzorci1, patch_artist = True, vert = True)

# Vodoravne črte
ax1.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.25)
ax1.set(axisbelow=True, title="Dohodki po četrtih", ylabel='Dohodki')

# Barve škatl
colors1 = ['#EF476F', '#FFD166', '#06D6A0', '#118AB2']
for patch, color in zip(bp1['boxes'], colors1):
    patch.set_facecolor(color)

# Brki, Min, maks, medijana, osamelci
for whisker in bp1['whiskers']:
    whisker.set(color ='#073B4C', linewidth = 1.5, linestyle =":")
 
for cap in bp1['caps']:
    cap.set(color ='#073B4C', linewidth = 2)
 
for median in bp1['medians']:
    median.set(color ='#073B4C', linewidth = 3)
 
for flier in bp1['fliers']:
    flier.set(marker ='o', color ='#073B4C')
     
# Oznake za x-os
ax1.set_xticklabels(['Severna četrt', 'Vzhodna četrt', 'Južna četrt', 'Zahodna četrt'])

# Prikaz grafa
plt.show()

# ----------------- b) naloga ----------------- #

vzorci2 = [enst_vrzc_S_dohodek]
for i in range(4):
    vzorci2.append(list(map(int, list(S_cetrt.sample(100, replace=False, random_state=(i+10)).DOHODEK))))

fig = plt.figure(figsize =(8, 6))
ax2 = fig.add_subplot(111)
bp2 = ax2.boxplot(vzorci2, patch_artist = True, vert = True)

# Vodoravne črte
ax2.yaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.25)
ax2.set(axisbelow=True, title="Vzorci dohodkov v severni četrti", ylabel='Dohodki')

# Barve škatl
colors2 = ['#EF476F', '#EF476F', '#EF476F', '#EF476F', '#EF476F']
for patch, color in zip(bp2['boxes'], colors2):
    patch.set_facecolor(color)

# Brki, Min, maks, medijana, osamelci
for whisker in bp2['whiskers']:
    whisker.set(color ='#073B4C', linewidth = 1.5, linestyle =":")
 
for cap in bp2['caps']:
    cap.set(color ='#073B4C', linewidth = 2)
 
for median in bp2['medians']:
    median.set(color ='#073B4C', linewidth = 3)
 
for flier in bp2['fliers']:
    flier.set(marker ='o', color ='#073B4C')
     
# Prikaz grafa
plt.show()


