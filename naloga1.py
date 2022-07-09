import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
oznake = ['TIP', 'CLANOV', 'OTROK', 'DOHODEK', 'CETRT', 'IZOBRAZBA']
n = 100
kibergrad = pd.read_csv('naloga/Kibergrad.csv', names=oznake)
cetrti = [kibergrad[kibergrad.CETRT == str(i)] for i in range(1,5)]

# ----------------- (a) naloga ----------------- #

seed = 2
vzorci1 = [list(map(int, list(cetrti[i].sample(n, replace=False, random_state=seed).DOHODEK))) for i in range(4)]

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
#plt.show()

# ----------------- (b) naloga ----------------- #

vzorci2 = vzorci1[:1]
for i in range(4):
    vzorci2.append(list(map(int, list(cetrti[0].sample(100, replace=False, random_state=(i+10)).DOHODEK))))

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
#plt.show()

# ----------------- (c) naloga ----------------- #

N = 43886
Ni = [10149, 10390, 13457, 9890]
wi = [x/N for x in Ni]
mui = [np.mean(list(map(int, list(cetrt.DOHODEK)))) for cetrt in cetrti]
mu = sum(wi[i]*mui[i] for i in range(4))
vari = [np.var(list(map(int, list(cetrt.DOHODEK)))) for cetrt in cetrti]

poj_var = round(sum([wi[i]*(mui[i] - mu)**2 for i in range(4)])) # 9252923
nepoj_var = round(sum([wi[i]*vari[i] for i in range(4)])) # 1017132747

print(f"S četrtmi pojasnjena varianca dohodka družin Kibergrada znaša {poj_var},\nresidualna varianca pa znaša {nepoj_var}.")
print(f"Pojasnjeni standardni odklon dohodka med četrtmi znaša {round(poj_var**0.5)}.")
print(f"Povprečni dohodki znašajo {round(mui[0])} v severni, {round(mui[1])} v vzhodni,\n{round(mui[2])} v južni in {round(mui[3])} v zahodni četrti.")