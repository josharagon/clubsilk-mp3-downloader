import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Setup: Replace these with your credentials and paths
username = "email"  # Replace with your username
password = "password"  # Replace with your password
chrome_driver_path = "chromeDrivePath"  # Update with ChromeDriver path
download_folder = "downloadFolderName"

os.makedirs(download_folder, exist_ok=True)

# Set up Chrome options
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Comment out or remove this line
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize the driver
driver = webdriver.Chrome(options=options)
driver.maximize_window()  # Optional: makes the window full size

try:
    # Step 1: Login
    login_url = "https://clubsilkrecords.com/login.php"
    driver.get(login_url)
    
    # Wait for page load
    time.sleep(3)
    
    # Login
    driver.find_element(By.NAME, "email").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    
    # Try multiple methods to find the login button
    try:
        # Method 1: By image source
        login_button = driver.find_element(By.CSS_SELECTOR, "input[src='/images/log-in_white.gif']")
    except:
        try:
            # Method 2: By alt text
            login_button = driver.find_element(By.CSS_SELECTOR, "input[alt='Click Here to Login']")
        except:
            # Method 3: Find all image inputs and click the first one
            login_button = driver.find_element(By.TAG_NAME, "input[type='image']")
    
    print("Found login button, attempting to click...")
    login_button.click()
    
    # Add longer wait and check for messages
    time.sleep(2)    
    print("Continuing with navigation...")
    
    
    # Step 2: Navigate to "My Club Silk Records"
    my_stuff_link = driver.find_element(By.CSS_SELECTOR, "a.clink[href='/mystuff.php']")
    my_stuff_link.click()
    time.sleep(2)
    
    # Step 3: Navigate to "My MP3's"
    mp3s_link = driver.find_element(By.CSS_SELECTOR, "a.mystuff[href='mymp3s.php']")
    mp3s_link.click()
    time.sleep(3)

    print("Current URL:", driver.current_url)
    
    def download_mp3s(driver):
        print("Finding download links...")
        download_links = driver.find_elements(By.CSS_SELECTOR, "a.uclink[href*='downloadmp3.php']")
        print(f"Found {len(download_links)} potential downloads")
        
        # Store all the download URLs first
        download_urls = [link.get_attribute('href') for link in download_links]
        
        for url in download_urls:
            try:
                # Navigate to the download page
                driver.get(url)
                time.sleep(2)  # Wait for new link to generate
                
                # Find the generated MP3 link
                mp3_link = driver.find_element(By.CSS_SELECTOR, "a.mystuff[href*='.mp3']")
                mp3_url = mp3_link.get_attribute('href')
                filename = mp3_url.split('/')[-1]
                
                print(f"Downloading: {filename}")
                # Download using requests to avoid Selenium issues
                response = requests.get(mp3_url)
                
                # Save to the download folder
                filepath = os.path.join(download_folder, filename)
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                print(f"Successfully downloaded: {filename}")
                
                # Go back to MP3s page
                driver.get("https://clubsilkrecords.com/mymp3s.php")
                time.sleep(1)
                
            except Exception as e:
                print(f"Error downloading track: {str(e)}")
                continue

    download_mp3s(driver)

finally:
    # Cleanup
    driver.quit()
