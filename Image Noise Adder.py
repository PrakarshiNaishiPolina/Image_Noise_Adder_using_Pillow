import random
from PIL import Image

def add_noise(image_path, output_path, noise_level):
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")  # Ensure image is in RGB format for manipulation

        pixels = img.load()  # Get access to pixel data

        # Apply the noise
        for i in range(img.width):
            for j in range(img.height):
                r, g, b = pixels[i, j]  # Get the current pixel's RGB values

                # Add random noise to each channel
                noise = lambda x: max(0, min(255, x + random.randint(-noise_level, noise_level)))
                pixels[i, j] = (noise(r), noise(g), noise(b))  # Assign the noisy pixel

        img.save(output_path)
        img.show()
        print(f"Image with noise saved at {output_path}")
    except Exception as e:
        print(f"Error: {e}")

# Call the function with appropriate parameters
add_noise(image_path="max verstappen (2).jpeg", output_path="noisy_image.jpg", noise_level=30)


