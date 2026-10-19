#JESUS ARRIAGA 
# NC = 0019
import os
import cv2
import matplotlib.pyplot as plt

# Imagen
# Vamos a crear nuestra matriz principal
ruta_img = os.path.join("img-original-0019", "img-BMW-0019.jpg")
img = cv2.imread(ruta_img)

# Corregimos
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Extraemos los canales
#R = img[:,:,0]
#G = img[:,:,1]
#B = img[:,:,2]

print(img)

# Comando
R,G,B = cv2.split(img)

# Mostramos nuestros canales
fig = plt.figure()

# CANAL ROJO (en tonos rojos)
ax1 = fig.add_subplot(2,2,1)
ax1.imshow(R, cmap="Reds")
ax1.set_title("CANAL ROJO")

# CANAL VERDE (en tonos verdes)
ax2 = fig.add_subplot(2,2,2)
ax2.imshow(G, cmap="Greens")
ax2.set_title("CANAL VERDE")

# CANAL AZUL (en tonos azules)
ax3 = fig.add_subplot(2,2,3)
ax3.imshow(B, cmap="Blues")
ax3.set_title("CANAL AZUL")

# RECONSTRUCCION
imgre = cv2.merge((R,G,B))

# IMAGEN ORIGINAL
ax4 = fig.add_subplot(2,2,4)
ax4.imshow(imgre)
ax4.set_title("IMAGEN ORIGINAL")
#plt.imshow(img)

# Guardamos la ventana de resultados en la carpeta correspondiente
os.makedirs("resultados-img-0019", exist_ok=True)
plt.savefig("resultados-img-0019/resultado-BMW-0019.jpg")

plt.show()

# Con el teclado pasamos la imagen
cv2.waitKey(0)
print("PROGRAMA REALIZADO POR JESUS ARRIAGA 0019")