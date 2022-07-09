import math
import matplotlib.pyplot as plt
import numpy as np

stSkokov = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
stOpazanj = [48, 31, 20, 9, 6, 5, 4, 2, 1, 1, 2, 1]

N = sum(stOpazanj)
S = sum([stSkokov[i]*stOpazanj[i] for i in range(len(stSkokov))])

# ----------------- (a) naloga ----------------- #

p = round(N/S, 3)

print(f"Pristranska cenilka za parameter geometrijske porazdelitve znaša {p}.")


# ----------------- (b) naloga ----------------- #

verjetnosti = []
pricakovane_frek = []
for k in stSkokov:
    temp = p
    for _ in range(k-1):
        temp *= (1-p)
    verjetnosti.append(round(temp, 4))
    pricakovane_frek.append(round(verjetnosti[k-1]*N, 2))
#print(verjetnosti)
#print(pricakovane_frek)

plt.plot(stSkokov, stOpazanj, color='red', marker='o', label="Opažene frekvence")
plt.plot(stSkokov, pricakovane_frek, color='blue', marker='o', label="Pričakovane frekvence")
plt.title('Črtni grafikon frekvenc 1')
plt.xlabel('Število skokov')
plt.ylabel('Frekvence')
plt.grid(True)
plt.legend()
plt.show()

# ----------------- (c) naloga ----------------- #

p2 = round((N-1)/(S-1), 3)
verjetnosti2 = []
pricakovane_frek2 = []
for k in stSkokov:
    temp = p2
    for _ in range(k-1):
        temp *= (1-p2)
    verjetnosti2.append(round(temp, 4))
    pricakovane_frek2.append(round(verjetnosti2[k-1]*N, 2))
#print(verjetnosti2)
#print(pricakovane_frek2)

print(f"Nepristranska cenilka za parameter geometrijske porazdelitve znaša {p2}.")

plt.plot(stSkokov, stOpazanj, color='red', marker='o', label="Opažene frekvence")
plt.plot(stSkokov, pricakovane_frek, color='blue', marker='o', label="Pričakovane frekvence pristranske cenilke")
plt.plot(stSkokov, pricakovane_frek2, color='green', marker='o', label="Pričakovane frekvence nepristranske cenilke")
plt.title('Črtni grafikon frekvenc 2')
plt.xlabel('Število skokov')
plt.ylabel('Frekvence')
plt.grid(True)
plt.legend()
plt.show()