from PIL import Image
import sys
from datetime import datetime

def resize_image(image_path, size, output_path):
    img = Image.open(image_path)
    img = img.resize(size)
    img.save(output_path)

if __name__ == "__main__":
    image_path = sys.argv[1]
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    
    resize_image(image_path, (1920, 1080), f'resized_image_{current_time}_1920_1080.jpg')
    resize_image(image_path, (640, 360), f'resized_image_{current_time}_640_360.jpg')
