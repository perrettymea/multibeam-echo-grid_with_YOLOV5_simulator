import numpy as np

nb_faisceau = np.array([333,354,383,409,460,486,513,543])

total = 880

ouverture = 130

angle_correspondants = nb_faisceau/total*ouverture -ouverture /2

print(angle_correspondants)

#Combien ça fait 0,3 degrés entre 12,7 et 13, projeté à 2000 en incertitude de position ? (x,z)

x_0 = np.sin(13*np.pi/180)*2000
z_0 = np.cos(13*np.pi/180)*2000

x_1 = np.sin(12.7*np.pi/180)*2000
z_1 = np.cos(12.7*np.pi/180)*2000

print(x_0-x_1,z_0-z_1)

##Incertitude de 10 m en x (ok incertitude levé).

ecartement = np.array([0.012,0.013,0.014,0.0145,0.015,0.0155,0.016,0.017,0.018])
print(ecartement)
erreur_cum = np.array([6.09863637, 3.59863637,2.44045455,2.08,1.83772727,1.65,1.95227275,3.60136363,3.98409091])

import matplotlib.pyplot as plt

plt.figure()
plt.plot(ecartement,erreur_cum)
plt.show()
