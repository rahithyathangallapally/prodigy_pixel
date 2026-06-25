from PIL import Image
import matplotlib.pyplot as plt

KEY = 150


def encrypt_image(input_image, output_image):
    img = Image.open(input_image)
    pixels = img.load()

    width, height = img.size

    print("Original First Pixel:", pixels[0, 0])

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            pixels[x, y] = (
                (r + KEY) % 256,
                (g + KEY) % 256,
                (b + KEY) % 256
            )

    print("Encrypted First Pixel:", pixels[0, 0])

    img.save(output_image)

    print("\n✓ Image Encrypted Successfully")
    print(f"✓ Saved as {output_image}")


def decrypt_image(input_image, output_image):
    img = Image.open(input_image)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            pixels[x, y] = (
                (r - KEY) % 256,
                (g - KEY) % 256,
                (b - KEY) % 256
            )

    print("Decrypted First Pixel:", pixels[0, 0])

    img.save(output_image)

    print("\n✓ Image Decrypted Successfully")
    print(f"✓ Saved as {output_image}")


def show_images():
    try:
        original = Image.open("sample.jpg")
        encrypted = Image.open("encrypted_image.png")
        decrypted = Image.open("decrypted_image.png")

        plt.figure(figsize=(12, 4))

        plt.subplot(1, 3, 1)
        plt.imshow(original)
        plt.title("Original Image")
        plt.axis("off")

        plt.subplot(1, 3, 2)
        plt.imshow(encrypted)
        plt.title("Encrypted Image")
        plt.axis("off")

        plt.subplot(1, 3, 3)
        plt.imshow(decrypted)
        plt.title("Decrypted Image")
        plt.axis("off")

        plt.tight_layout()
        plt.show()

    except FileNotFoundError:
        print("\nPlease encrypt and decrypt the image first.")


while True:

    print("\n========== IMAGE ENCRYPTION TOOL ==========")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    print("3. Show Images")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        image_name = input("Enter image filename (example: sample.jpg): ")
        encrypt_image(image_name, "encrypted_image.png")

    elif choice == "2":
        decrypt_image("encrypted_image.png", "decrypted_image.png")

    elif choice == "3":
        show_images()

    elif choice == "4":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")