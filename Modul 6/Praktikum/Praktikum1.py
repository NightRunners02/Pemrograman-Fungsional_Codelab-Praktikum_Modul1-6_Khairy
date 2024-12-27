import cv2
import numpy as np
import matplotlib.pyplot as plt

from google.colab import files
uploaded = files.upload()

image_path = next(iter(uploaded))
image = cv2.imread(image_path)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

alpha = 1.2
beta = 50

adjusted = cv2.convertScaleAbs(image_rgb, alpha=alpha, beta=beta)

hsv = cv2.cvtColor(adjusted, cv2.COLOR_RGB2HSV)
h, s, v = cv2.split(hsv)
s = cv2.add(s, 100)
s = np.clip(s, 0, 255)
final_hsv = cv2.merge((h, s, v))
final_image = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2RGB)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Gambar Awal')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Gambar Kedua')
plt.imshow(final_image)
plt.axis('off')

plt.show()
