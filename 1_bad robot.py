import cv2
import numpy as np

# Crear un lienzo negro
canvas = np.zeros((500, 700, 3), dtype=np.uint8)

# Dibujar el cuerpo del robot (forma rectangular en rojo)
cv2.rectangle(canvas, (250, 150), (450, 300), (0, 0, 200), -1)  # Relleno rojo
cv2.rectangle(canvas, (250, 150), (450, 300), (0, 0, 0), 2)     # Borde negro

# Dibujar el resorte en la parte superior
spring_center = 350
spring_top = 100
spring_height = 50
cv2.line(canvas, (spring_center, spring_top+spring_height), (spring_center, 150), (100, 100, 100), 3)

# Dibujar el resorte (simplificado)
for i in range(spring_top, spring_top+spring_height, 8):
    cv2.line(canvas, (spring_center-10, i), (spring_center+10, i+4), (100, 100, 100), 2)
    cv2.line(canvas, (spring_center+10, i+4), (spring_center-10, i+8), (100, 100, 100), 2)

# Dibujar los ojos (círculos amarillos)
# Ojo izquierdo
cv2.circle(canvas, (300, 200), 25, (0, 0, 0), 2)     # Borde negro
cv2.circle(canvas, (300, 200), 23, (0, 255, 255), -1)  # Relleno amarillo

# Ojo derecho
cv2.circle(canvas, (400, 200), 25, (0, 0, 0), 2)     # Borde negro
cv2.circle(canvas, (400, 200), 23, (0, 255, 255), -1)  # Relleno amarillo

# Dibujar la nariz triangular
nariz = np.array([
    [350, 220],  # Punta superior
    [340, 240],  # Esquina inferior izquierda
    [360, 240]   # Esquina inferior derecha
], np.int32)
nariz = nariz.reshape((-1, 1, 2))
cv2.fillPoly(canvas, [nariz], (0, 0, 0))  # Negro

# Mostrar la imagen
cv2.imshow('Bad Robot Practica', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
