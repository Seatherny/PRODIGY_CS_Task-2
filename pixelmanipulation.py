from PIL import Image


def encrypt_image(input_path, output_path, key=None):

    # Swapping color channels (red and blue) for encryption
    img = Image.open(output_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            encrypted_pixel = (g, b, r)
            pixels[i, j] = encrypted_pixel

    img.save(output_path)
    print("Image encrypted successfully!")

def decrypt_image(input_path, output_path, key=None):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            decrypted_pixel = (g, b, r)
            pixels[i, j] = decrypted_pixel

    img.save(output_path)
    print("Image decrypted successfully!")

# Image paths
input_image = r"/Users/idckgaf/chhavi/wallpaper/Screenshot 2023-04-19 at 3.36.07 PM.png"
encrypted_image = r"/Users/idckgaf/chhavi/wallpaper/Screenshot_encrypted.png"
decrypted_image = r"/Users/idckgaf/chhavi/wallpaper/Screenshot_decrypted.png"

# Encrypt the image
encrypt_image(input_image, encrypted_image, key=None)

# Decrypt the image
decrypt_image(encrypted_image, decrypted_image, key=None)