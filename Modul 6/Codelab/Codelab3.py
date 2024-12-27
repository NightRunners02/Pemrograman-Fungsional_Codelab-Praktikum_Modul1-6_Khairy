from google.colab import files
from google.colab import drive
from PIL import Image
import matplotlib.pyplot as plt
import os

drive.mount('/content/drive')

drive_save_path = "/content/drive/My Drive/overlay_result.png"

print("Unggah file background Anda:")
uploaded_bg = files.upload()
background_file = list(uploaded_bg.keys())[0]

print("Unggah file overlay Anda:")
uploaded_ov = files.upload()
overlay_file = list(uploaded_ov.keys())[0]

background_image = Image.open(background_file)
overlay_image = Image.open(overlay_file)

overlay_image = overlay_image.convert("RGB")

overlay_image = overlay_image.resize((400, 400))

bg_width, bg_height = background_image.size
ov_width, ov_height = overlay_image.size
x_center = (bg_width - ov_width) // 2
y_center = (bg_height - ov_height) // 2

background_image.paste(overlay_image, (x_center, y_center))

background_image.save(drive_save_path)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Background")
plt.imshow(Image.open(background_file))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Result with Overlay")
plt.imshow(background_image)
plt.axis('off')

plt.tight_layout()
plt.show()

print(f"Gambar hasil edit telah disimpan di Google Drive sebagai: {drive_save_path}")
