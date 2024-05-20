from PIL import Image

# Function to encrypt the image
def encrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size
    pixels = img.load()

    encrypted_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Example operation: XOR with the key
            r ^= key
            g ^= key
            b ^= key
            encrypted_pixels.append((r, g, b))

    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(encrypted_pixels)
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully!")

# Function to decrypt the image
def decrypt_image(encrypted_image_path, key):
    img = Image.open(encrypted_image_path)
    width, height = img.size
    pixels = img.load()

    decrypted_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            # Reverse the encryption operation
            r ^= key
            g ^= key
            b ^= key
            decrypted_pixels.append((r, g, b))

    decrypted_img = Image.new(img.mode, img.size)
    decrypted_img.putdata(decrypted_pixels)
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully!")

# Example usage
image_path = "input_image.png"
key = 123  # Example key

# Encrypt the image
encrypt_image(image_path, key)

# Decrypt the encrypted image
decrypt_image("encrypted_image.png", key)
