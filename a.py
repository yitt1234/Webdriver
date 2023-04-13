import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
# create a new instance of the Chrome driver

def driver():
  driver = webdriver.Chrome()
  driver.get("https://textstorage.netlify.app/login.html")

# find the input element by ID and enter some text
  email = driver.find_element(By.ID, 'signUpEmail')
  email.send_keys("gyogaga@gmail.com")
  ps = driver.find_element(By.ID, 'signUpPassword')
  ps.send_keys("gyogagi")
  signup = driver.find_element(By.ID, 'signUpButton')
  signup.click()
  input()
# close the browser window

call_time = datetime.time(19, 26, 40) # 5:00 PM

while True:
    # Get the current time
    current_time = datetime.datetime.now().time()

    # Compare the current time with the call time
    if current_time >= call_time:
        # Call the function and exit the loop
        driver()
        break

    # Wait for 1 second before checking the time again
    time.sleep(1)
input()