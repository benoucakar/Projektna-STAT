import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

podatki = pd.read_csv('naloga/Pulz.csv')
podatki['RAZLIKA_PULZOV'] = podatki.PULZ2 - podatki.PULZ1

# ----------------- (a) naloga ----------------- #
obremenjeni = podatki[podatki.OBREMENITEV == 1]
neobremenjeni = podatki[podatki.OBREMENITEV == 2]

n = len(obremenjeni)
m = len(neobremenjeni)
muX =np.mean(obremenjeni.RAZLIKA_PULZOV)
muY = np.mean(neobremenjeni.RAZLIKA_PULZOV)
sp2 = (n*np.var(obremenjeni.RAZLIKA_PULZOV) + m*np.var(neobremenjeni.RAZLIKA_PULZOV))/(m+n-2)
t = round((muX-muY)/(sp2*(1/n + 1/m))**(0.5),5)

print(f"Studentova statistika znaša {t} in ima {n+m-2} prostorskih stopenj.")

# ----------------- (b) naloga ----------------- #

razlika_pulzov_obremenjeni = obremenjeni.RAZLIKA_PULZOV
n = len(razlika_pulzov_obremenjeni)
[q1,q3] = razlika_pulzov_obremenjeni.quantile([.25, .75])
IQR = q3-q1
sirina = round(2.6 * IQR / (n**(1 / 3)),3)
bins = int(math.ceil((razlika_pulzov_obremenjeni.max() - razlika_pulzov_obremenjeni.min()) / sirina))

plt.hist(razlika_pulzov_obremenjeni, bins=bins)
plt.xlabel('Sprememba pulza')
plt.ylabel('Frekvenca')
plt.title('Histogram spremebe pulzov')
#plt.show() 

print(f"Širina stolpcev po modificiranem Freedman-Diaconisovem pravilu znaša {sirina}.")

# ----------------- (c) naloga ----------------- #

vadba1 = obremenjeni[obremenjeni.VADBA == 1].RAZLIKA_PULZOV 
vadba2 = obremenjeni[obremenjeni.VADBA == 2].RAZLIKA_PULZOV 
vadba3 = obremenjeni[obremenjeni.VADBA == 3].RAZLIKA_PULZOV 
N1 = len(vadba1)
N2 = len(vadba2)
N3 = len(vadba3)
k = 3
N = N1 + N2 + N3
mu1 = np.mean(vadba1)
mu2 = np.mean(vadba2)
mu3 = np.mean(vadba3)
mu = np.mean(pd.concat([vadba1,vadba2,vadba3]))

SSB = N1*(mu1 - mu)**2 + N2*(mu2 - mu)**2 + N3*(mu3 - mu)**2
SSW = N1*np.var(vadba1) + N2*np.var(vadba2) + N3*np.var(vadba3)

F = round((SSB/(k-1))/(SSW/(N-k)),5)

print(f"Studentova statistika znaša {F} in ima ({k-1}, {N-k}) prostorskih stopenj.")