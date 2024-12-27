from google.colab import files, drive
from PIL import Image
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
import numpy as np
import os

drive.mount('/content/drive')

save_path = "/content/drive/My Drive/Colab Outputs"
os.makedirs(save_path, exist_ok=True)

uploaded = files.upload()

for filename in uploaded.keys():
    img = Image.open(filename)

img_array = np.array(img)

gaussian_filtered = gaussian_filter(img_array, sigma=5)

fig, ax = plt.subplots(1, 4, figsize=(15, 5))
fig.suptitle("Codelab 2", fontsize=16, color="blue")

ax[0].imshow(img)
ax[0].set_title("Original Image")
ax[0].axis("off")

ax[1].imshow(img)
ax[1].text(10, 10, "Teks Contoh", fontsize=14, color="white", backgroundcolor="black")
ax[1].annotate("Anotasi", xy=(50, 50), xytext=(100, 100), fontsize=12,
               arrowprops=dict(facecolor="red", arrowstyle="->"))
ax[1].set_title("Teks dan Anotasi")
ax[1].axis("off")

rotated_img = img.rotate(45)
ax[2].imshow(rotated_img)
ax[2].set_title("Rotated (45°)")
ax[2].axis("off")

ax[3].imshow(gaussian_filtered.astype('uint8'))
ax[3].set_title("Gaussian Filter")
ax[3].axis("off")

output_file = os.path.join(save_path, "kucing.png")
plt.tight_layout()
plt.savefig(output_file, dpi=300)
print(f"Gambar telah disimpan ke Google Drive: {output_file}")

plt.show()
