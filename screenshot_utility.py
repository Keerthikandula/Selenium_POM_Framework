import os
from datetime import datetime

def take_screenshot(driver, name="screenshot"):
    # Create a directory for screenshots if it doesn't exist
    folder = "screenshots"
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Generate a timestamp for the screenshot filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = f"{folder}/{name}_{timestamp}.png"


    # Take the screenshot and save it to the specified path
    driver.save_screenshot(filepath)
    print(f"Screenshot saved : {filepath}")