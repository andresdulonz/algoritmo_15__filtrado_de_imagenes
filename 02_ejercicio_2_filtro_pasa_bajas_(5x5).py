import cv2
import numpy as np

#filtro pasa bajas (5x5) 1/25
f = np.array(([[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]]), np.float32)/25

im= cv2.imread('autopista.jpg')

#aplicamos el filtro
im2 = cv2.filter2D(im, -1, f)

cv2.imshow('imagen0', im)
cv2.imshow('imagen1', im2)
cv2.imwrite('02_imagen_pasa_bajas_(5x5).jpg', im2)
cv2.waitKey(0)

