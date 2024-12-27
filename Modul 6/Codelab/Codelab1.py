from google.colab import files
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

uploaded = files.upload()

for filename in uploaded.keys():
    img = Image.open(filename)

gambar_contour = img.filter(ImageFilter.CONTOUR)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Before :")
plt.imshow(img)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("After :")
plt.imshow(gambar_contour)
plt.axis('off')

plt.tight_layout()
plt.show()
