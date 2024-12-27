from PIL import Image, ImageEnhance, ImageFilter
import matplotlib.pyplot as plt
import numpy as np
from google.colab import files

uploaded = files.upload()
image_path = list(uploaded.keys())[0]

img = Image.open(image_path)

enhancer_color = ImageEnhance.Color(img)
img_enhanced_color = enhancer_color.enhance(2.0)

enhancer_brightness = ImageEnhance.Brightness(img_enhanced_color)
img_bright = enhancer_brightness.enhance(1.2)

enhancer_contrast = ImageEnhance.Contrast(img_bright)
img_contrast = enhancer_contrast.enhance(1.5)

img_filtered = img_contrast.filter(ImageFilter.EDGE_ENHANCE)

width, height = img_filtered.size
left = width * 0.1
top = height * 0.2
right = width * 0.7
bottom = height * 0.8
img_cropped = img_filtered.crop((left, top, right, bottom))

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.axis('off')
plt.imshow(img)

plt.subplot(1, 2, 2)
plt.title("Edited and Cropped Image")
plt.axis('off')
plt.imshow(img_cropped)

plt.tight_layout()
plt.show()

img_cropped.save("processed_image_cropped.png")