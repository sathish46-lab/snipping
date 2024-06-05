from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    # Open an image file
    with Image.open(input_path) as img:
        # Convert image to numpy array
        data = np.array(img)
        
        # Encrypt the image by applying a mathematical operation (XOR in this case) with the key
        encrypted_data = data ^ key
        
        # Create a new image from the encrypted data
        encrypted_img = Image.fromarray(encrypted_data)
        
        # Save the encrypted image
        encrypted_img.save(output_path)
        print(f"Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    # Open an image file
    with Image.open(input_path) as img:
        # Convert image to numpy array
        data = np.array(img)
        
        # Decrypt the image by applying the inverse operation (XOR with the same key)
        decrypted_data = data ^ key
        
        # Create a new image from the decrypted data
        decrypted_img = Image.fromarray(decrypted_data)
        
        # Save the decrypted image
        decrypted_img.save(output_path)
        print(f"Image decrypted and saved as {output_path}")

# Example usage
key = 123  # Simple encryption key (integer)

# Encrypt the image
encrypt_image('input_image.png', 'encrypted_image.png', key)

# Decrypt the image
decrypt_image('encrypted_image.png', 'decrypted_image.png', key)
