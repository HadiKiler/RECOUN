import subprocess
from pathlib import Path
import os
from selenium import webdriver
from PIL import Image
import os
import time
from selenium import webdriver
from django.core.files.base import ContentFile

            

def go_witness(url, path, type = 'png'):
    """insert just path object \n
        type: png or pdf """
    
    Path(path).mkdir(parents=True, exist_ok=True)
    image_path = os.path.join(path, f'{url}.png')
    # Create a new instance of the Firefox driver
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')

        driver = webdriver.Chrome(options=options)

        # Go to the Google website
        driver.get(f'https://{url}')

        time.sleep(1)
        # Take a screenshot of the webpage
        driver.save_screenshot(image_path)

        # Close the driver
        driver.quit()
        return image_path 
    except:
        return ""

    


















