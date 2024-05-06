import cv2
from src.estimate_watermark import *

gx, gy, gxlist, gylist = estimate_watermark('./images/fotolia_processed')

cropped_gx, cropped_gy = crop_watermark(gx, gy)
W_m = poisson_reconstruct(cropped_gx, cropped_gy)

plt.imshow(W_m)
plt.show()


