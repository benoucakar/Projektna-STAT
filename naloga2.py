# Pripadajočo porazdelitev določimo na podlagi metide verjetij.

p = 0.358
S = 130

ver = []
pric = []
for k in range(1,13):
    temp = p
    for _ in range(k-1):
        temp *= (1-p)
    ver.append(round(temp, 4))
    pric.append(round(ver[k-1]*S,2))
print(ver)
print(pric)


import matplotlib.pyplot as plt
   
stSkokov = [1,2,3,4,5,6,7,8,9,10,11,12]
opazene = [48, 31, 20, 9, 6, 5, 4, 2, 1, 1, 2, 1]
predvidene = pric
  
plt.plot(stSkokov, opazene, color='red', marker='o', label="Opažene vrednosti")
plt.plot(stSkokov, predvidene, color='blue', marker='o', label="Pričakovane vrednsoti")
plt.title('Črtni grafikon frekvenc')
plt.xlabel('Število skokov')
plt.ylabel('Frekvenca')
plt.grid(True)
plt.legend()
plt.show()
