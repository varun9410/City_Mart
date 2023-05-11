import requests

def send_image(image_path):
    api_url = 'http://127.0.0.1:5000/find_product'  # Replace with your API endpoint URL

    # Open the image file in binary mode
    with open(image_path, 'rb') as file:
        # Create a dictionary with the file data
        files = {'image': file}

        # Send a POST request to the API endpoint with the image file
        response = requests.post(api_url, files=files)

        # Check the response status code
        if response.status_code == 200:
            # Handle the API response
            api_response = response.json()
            # Process the response as needed
            return api_response

    # Return None or raise an exception if the request fails
    return None

# Example usage
image_path = '/workspaces/City_Mart/media/product_image/images/61RpRYFb2wL._SL1100_.jpg'  # Replace with the path to your image file
api_response = send_image(image_path)

if api_response is not None:
    # Process the API response
    print(api_response)
else:
    print('Image upload failed!')
