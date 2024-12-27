from google.colab import files
from PIL import Image, ImageEnhance, ImageFilter, ImageOps, ImageDraw, ImageFont
import matplotlib.pyplot as plt

def manipulate_image(image_path, watermark_text):
    image = Image.open(image_path)

    enhancer = ImageEnhance.Brightness(image)
    bright_image = enhancer.enhance(1.3)

    bright_image_resized = bright_image.resize((300, 300))

    image_with_border = ImageOps.expand(bright_image_resized, border=10, fill='white')

    image_with_sharpening = image_with_border.filter(ImageFilter.SHARPEN)

    grayscale_image = image_with_sharpening.convert('L')

    draw = ImageDraw.Draw(grayscale_image)
    font = ImageFont.load_default()

    width, height = grayscale_image.size
    text_bbox = draw.textbbox((0, 0), watermark_text, font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    offset = (1, 1)
    draw.text((width - text_width - 10 + offset[0], height - text_height - 10 + offset[1]), watermark_text, font=font, fill='black')

    output_path = "/content/output_image.jpg"
    grayscale_image.save(output_path)

    return image, bright_image, grayscale_image, output_path

def show_comparison(original_image, bright_image, manipulated_image):
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    axes[0].imshow(original_image)
    axes[0].set_title("Gambar Asli")
    axes[0].axis('off')

    axes[1].imshow(bright_image)
    axes[1].set_title("Gambar 30% Kecerahan")
    axes[1].axis('off')

    axes[2].imshow(manipulated_image, cmap='gray')
    axes[2].set_title("Gambar Manipulasi")
    axes[2].axis('off')

    plt.show()

uploaded = files.upload()

image_path = next(iter(uploaded))
watermark_text = "Toko Night"

original_image, bright_image, manipulated_image, output_path = manipulate_image(image_path, watermark_text)

show_comparison(original_image, bright_image, manipulated_image)

files.download(output_path)
