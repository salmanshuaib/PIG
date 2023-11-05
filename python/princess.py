from PIL import Image, ImageDraw
import random
import time

# Load the image
image_path = 'PRINCESS.PNG'
img = Image.open(image_path)
draw = ImageDraw.Draw(img)

# Define the coordinates of the squares where you want to simulate flashing
squares = [
    (45, 45, 90, 90),  # Example coordinates of the first square (adjust as needed)
    # Add the coordinates for the remaining squares
]

while True:
    # Randomly select a square
    selected_square = random.choice(squares)

    # Clear the square by redrawing it with a black rectangle
    x1, y1, x2, y2 = selected_square
    draw.rectangle((x1, y1, x2, y2), fill='black')

    # Save the modified image
    img.save('Supergirl.jpg')

    # Sleep for 1 second before restoring the square
    time.sleep(1)

    # Restore the original content of the square (e.g., by reloading the image)
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # Save the updated image
    img.save('Supergirl.png')
