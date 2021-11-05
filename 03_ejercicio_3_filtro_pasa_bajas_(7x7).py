import cv2
import numpy as np

#filtro pasa bajas (7x7) 1/49
f = np.ones((7,7))/49

im= cv2.imread('autopista.jpg')

#aplicamos el filtro
im2 = cv2.filter2D(im, -1, f)

cv2.imshow('imagen0', im)
cv2.imshow('imagen1', im2)
cv2.imwrite('03_imagen_pasa_bajas_(7x7).jpg', im2)
cv2.waitKey(0)

