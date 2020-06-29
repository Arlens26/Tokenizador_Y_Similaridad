import math
import numpy as np 
import matplotlib.pyplot as plt

# Declaración de vectores
doc1 = np.array([27,14])
doc2 = np.array([4,0])
doc3 = np.array([24,17])
q = np.array([13,22]) # car, auto, insure y best
#d = np.array([doc1,doc2,doc3])
# Número de términos
#N = d.shape[0]
#print("Número de términos: "+str(N))

print("## Función Sim(q,d) sobre los términos car y best")

prod_punto_doc1 = q[0]*doc1[0] + q[1]*doc1[1]
raiz_prod_punto_doc1 = np.sqrt(q[0]*(doc1[0]*doc1[0])+(q[1]*doc1[1]*doc1[1]))
sim_doc1 = prod_punto_doc1/raiz_prod_punto_doc1
print("Sim(q,doc1): ",sim_doc1)

prod_punto_doc2 = q[0]*doc2[0] + q[1]*doc2[1]
raiz_prod_punto_doc2 = np.sqrt(q[0]*(doc2[0]*doc2[0])+(q[1]*doc2[1]*doc2[1]))
sim_doc2 = prod_punto_doc2/raiz_prod_punto_doc2
print("Sim(q,doc2): ",sim_doc2)

prod_punto_doc3 = q[0]*doc3[0] + q[1]*doc3[1]
raiz_prod_punto_doc3 = np.sqrt(q[0]*(doc3[0]*doc3[0])+(q[1]*doc3[1]*doc3[1]))
sim_doc3 = prod_punto_doc3/raiz_prod_punto_doc3
print("Sim(q,doc3): ",sim_doc3)

print("## Similaridad del coseno")
car = np.array([27,4,24])
best = np.array([14,0,17])
sum_prod_punto = car[0]*best[0] + car[1]*best[1] + car[2]*best[2]
prod_raiz = (np.sqrt(car[0]*car[0]+car[1]*car[1]+car[2]*car[2]) * np.sqrt((best[0]*best[0]+best[1]*best[1]+best[1]*best[1])))
coseno = sum_prod_punto/prod_raiz
print("Cosine(car,best):",coseno)

sum_doc1 = q[0]*doc1[0] + q[1]*doc1[1] + q[1]*doc1[1]
prod_raiz_doc1 = (np.sqrt(q[0]*q[0]+q[1]*q[1]) * np.sqrt((doc1[0]*doc1[0]+doc1[1]*doc1[1]+doc1[1]*doc1[1])))
coseno1 = sum_doc1/prod_raiz_doc1
print("Cosine(q,doc1):",coseno1)

sum_doc2 = q[0]*doc2[0] + q[1]*doc2[1] + q[1]*doc2[1]
prod_raiz_doc2 = (np.sqrt(q[0]*q[0]+q[1]*q[1]) * np.sqrt((doc2[0]*doc2[0]+doc2[1]*doc2[1]+doc2[1]*doc2[1])))
coseno2 = sum_doc2/prod_raiz_doc2
print("Cosine(q,doc2):",coseno2)

sum_doc3 = q[0]*doc3[0] + q[1]*doc3[1] + q[1]*doc3[1]
prod_raiz_doc3 = (np.sqrt(q[0]*q[0]+q[1]*q[1]) * np.sqrt((doc3[0]*doc3[0]+doc3[1]*doc3[1]+doc3[1]*doc3[1])))
coseno3 = sum_doc3/prod_raiz_doc3
print("Cosine(q,doc3):",coseno3)

#plt.plot(sim[i],0)

# Dibujo de vectores
#plt.plot(2,2, linewidth=4)
plt.quiver(0, 0, q[0], q[1],  angles='xy', scale_units='xy', scale=1, color="r")
plt.quiver(0, 0, doc1[0], doc1[1],  angles='xy', scale_units='xy', scale=1, color="g")
plt.quiver(0, 0, doc2[0], doc2[1],  angles='xy', scale_units='xy', scale=1, color="b")
plt.quiver(0, 0, doc3[0], doc3[1], angles='xy', scale_units='xy', scale=1)
plt.show()

