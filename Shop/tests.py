from django.test import TestCase
import requests

image_path = '/home/varun/City_Mart/media/product_image/images/61bVorIFk6L._UY625_.jpg'  # Replace with the actual path to your image file

# Open the image file and read its contents
with open(image_path, 'rb') as file:
    image_data = file.read()

# Send a POST request with the image data
response = requests.post('https://varun9410-psychic-eureka-x77p5q6rxqcv6x4-8000.preview.app.github.dev/127.0.0.1/find_product',files={'image': image_data})

# Check the response
if response.status_code == 200:
    result = response.json()
    # Process the result as needed
    print(result)
else:
    print('Error:', response.status_code)
