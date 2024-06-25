
from PIL import Image
import requests


def savepictofile(path, img):
    try:
        with open(path, 'wb') as file:
            file.write(img.screenshot_as_png)
        return True
    except:
        return False

#проверяет размеры и пропорции сохраненного изображения
def conditions(path):
    try:
        with Image.open(path) as img:
            width, height = img.size
            proportion = width / height
            if (width > 800) and (height > 500) and (1.31 <= proportion <= 1.9):
                return True
            else:
                return False

    except:
        return False

def save_image(img_url, path):
    try:
        print(f"Downloading image from: {img_url}")
        print(f"Saving to: {path}")

        # Send a GET request to the image URL
        response = requests.get(img_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            with open(path, 'wb') as file:
                file.write(response.content)
            print(f"Image saved successfully at {path}")
        else:
            print(f"Failed to download the image. HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        # Handle any requests-related exceptions
        print(f"Error occurred while downloading the image: {e}")
    except IOError as e:
        # Handle file I/O errors
        print(f"Error occurred while saving the image: {e}")
    except Exception as e:
        # Handle any other exceptions
        print(f"An unexpected error occurred: {e}")


