import cv2
import numpy as np

#filtro pasa bajas (3x3) 1/9
f = np.array(([[1,1,1], [1,1,1], [1,1,1]]), np.float32)/9

im= cv2.imread('autopista.jpg')

#aplicamos el filtro
im2 = cv2.filter2D(im, -1, f)

cv2.imshow('imagen0', im)
cv2.imshow('imagen1', im2)
cv2.imwrite('01_imagen_pasa_bajas_(3x3).jpg', im2)
cv2.waitKey(0)

