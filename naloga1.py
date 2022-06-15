import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
pd.options.display.max_rows = 20

kibergrad = pd.read_csv('naloga/Kibergrad.csv', names=['TIP', 'CLANOV', 'OTROK', 'DOHODEK', 'CETRT', 'IZOBRAZBA'])
S_cetrt = kibergrad[kibergrad.CETRT == "1"]
V_cetrt = kibergrad[kibergrad.CETRT == "2"]
J_cetrt = kibergrad[kibergrad.CETRT == "3"]
Z_cetrt = kibergrad[kibergrad.CETRT == "4"]

# ----------------- a) naloga ----------------- #

enst_vrzc_S_dohodek = list(map(int, list(S_cetrt.sample(100, replace=False, random_state=2).DOHODEK)))
enst_vrzc_V_dohodek = list(map(int,list(V_cetrt.sample(100, replace=False, random_state=2).DOHODEK)))
enst_vrzc_J_dohodek = list(map(int,list(J_cetrt.sample(100, replace=False, random_state=2).DOHODEK)))
enst_vrzc_Z_dohodek = list(map(int,list(Z_cetrt.sample(100, replace=False, random_state=2).DOHODEK)))

vzorci1 = [enst_vrzc_S_dohodek, enst_vrzc_V_dohodek, enst_vrzc_J_dohodek, enst_vrzc_Z_dohodek]

fig = plt.figure(figsize =(15, 10))
ax1 = fig.add_subplot(111)
bp1 = ax1.boxplot(vzorci1, patch_artist = True, vert = False)

# Vodoravne črte
ax1.xaxis.grid(True, linestyle='-', which='major', color='lightgrey', alpha=0.25)
ax1.set(axisbelow=True, title="Dohodki po četrtih", xlabel='Dohodki')

# Barve škatl
colors = ['#EF476F', '#FFD166', '#06D6A0', '#118AB2']
for patch, color in zip(bp1['boxes'], colors):
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
ax1.set_yticklabels(['Severna četrt', 'Vzhodna četrt', 'Južna četrt', 'Zahodna četrt'])

# Prikaz grafa
plt.show()

# ----------------- b) naloga ----------------- #

enst_vrzc_S_dohodek2 = list(map(int, list(S_cetrt.sample(100, replace=False, random_state=2).DOHODEK)))
enst_vrzc_S_dohodek3 = list(map(int, list(S_cetrt.sample(100, replace=False, random_state=2).DOHODEK)))
enst_vrzc_S_dohodek4 = list(map(int, list(S_cetrt.sample(100, replace=False, random_state=2).DOHODEK)))
enst_vrzc_S_dohodek5 = list(map(int, list(S_cetrt.sample(100, replace=False, random_state=2).DOHODEK)))

vzorci2 = [enst_vrzc_S_dohodek, enst_vrzc_S_dohodek2, enst_vrzc_S_dohodek3, enst_vrzc_S_dohodek4, enst_vrzc_S_dohodek5]

# Test
