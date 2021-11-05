import cv2
import numpy as np

#filtro pasa altas (3x3)
f = np.array(([[0,-1,0], [-1,4,-1], [0,-1,0]]), np.float32)

im= cv2.imread('autopista.jpg',0)

#aplicamos el filtro
im2 = cv2.filter2D(im, -1, f)

cv2.imshow('imagen0', im)
cv2.imshow('imagen1', im2)
cv2.imwrite('05_imagen_pasa_altas_(3x3)_gis.jpg', im2)
cv2.waitKey(0)

