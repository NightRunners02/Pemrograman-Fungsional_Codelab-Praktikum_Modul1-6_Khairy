from google.colab import files
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

print("Unggah file gambar Anda:")
uploaded = files.upload()

file_name = list(uploaded.keys())[0]

try:

    img = Image.open(file_name)


    fig, ax = plt.subplots(2, 2, figsize=(10, 10))

    ax[0, 0].imshow(img)
    ax[0, 0].set_title("Gambar Asli", fontsize=16)
    ax[0, 0].axis("off")

    ax[0, 1].imshow(img)
    ax[0, 1].text(10, 10, "Teks Contoh", fontsize=14, color="white", backgroundcolor="black")
    ax[0, 1].annotate("Anotasi", xy=(50, 50), xytext=(100, 100), fontsize=12,
                      arrowprops=dict(facecolor="red", arrowstyle="->"))
    ax[0, 1].set_title("Teks dan Anotasi")
    ax[0, 1].axis("off")

    rotated_img = img.rotate(45)
    ax[1, 0].imshow(rotated_img)
    ax[1, 0].set_title("Rotasi 45 Derajat")
    ax[1, 0].axis("off")

    filtered_img = img.filter(ImageFilter.CONTOUR)
    output_filename = "filtered_image.jpg"
    filtered_img.save(output_filename)
    ax[1, 1].imshow(filtered_img)
    ax[1, 1].set_title("Filtered: CONTOUR")
    ax[1, 1].axis("off")

    plt.tight_layout()
    plt.show()

    print("Mengunduh gambar hasil edit...")
    files.download(output_filename)

    from google.colab import drive
    drive.mount('/content/drive')
    drive_output_path = "/content/drive/My Drive/filtered_image.jpg"
    filtered_img.save(drive_output_path)
    print(f"Gambar juga disimpan di Google Drive: {drive_output_path}")

except Exception as e:
    print(f"Terjadi kesalahan: {e}")