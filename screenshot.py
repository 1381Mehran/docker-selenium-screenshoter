import os
import time
import argparse

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def parse_arguments() -> None:
    parser = argparse.ArgumentParser(description="Take screenshots of multiple URLs using Selenium.")
    parser.add_argument('urls', nargs='+', help="List of URLs to take screenshots of")
    return parser.parse_args()

def take_screenshots(url: str) -> None:
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')  # Avoids issues in Docker

    # Connect to the Selenium Docker container
    CHROME_URL = 'http://localhost:4444/wd/hub'

    try:
        driver = webdriver.Remote(
            command_executor=CHROME_URL,
            options=chrome_options
        )

        # Navigate to the website
        print(f"Accessing URL: {url}")
        driver.get(url)

        # Wait for the page to load
        time.sleep(2)

        # Take a screenshot
        screenshot_name = f'screenshot_{url.split("//")[-1].replace("/", "_").replace(".", "_").replace(":", "_")}.png'
        
        screenshots_dir = os.path.join(os.getcwd(), 'screenshots')
        if not os.path.exists(screenshots_dir):
            os.makedirs(screenshots_dir)
        
        screenshot_path = os.path.join(screenshots_dir, screenshot_name)

        driver.save_screenshot(screenshot_path)

        print(f"Screenshot taken and saved as {screenshot_name}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the driver
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    args = parse_arguments()
    print(f"URLs to process: {args.urls}")

    for url in args.urls:
        take_screenshots(url)