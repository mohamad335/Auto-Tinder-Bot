from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep

FB_EMAIL = "facebook email or phone number"
FB_PASSWORD = "your password"

driver = webdriver.Chrome()
driver.get("http://www.tinder.com")
sleep(2)
#first we click on login and choose facebook login
login_button = driver.find_element(By.XPATH, value='//*[text()="Log in"]')
login_button.click()
sleep(2)

fb_login = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()
"""The Facebook login page opens in a new window.
 In order for our selenium code to work on the new window,
 we have to switch to the window in front."""
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.XPATH, value='//*[@id="email"]')
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')
email.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

#Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)
sleep(5)

#Allow location
allow_location_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

#Disallow notifications
disallow_notifications_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
disallow_notifications_button.click()

#Allow cookies
allow_cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
allow_cookies.click()
#since we can't make like more than 100
for n in range(100):

    #Add a 1 second delay between likes.
    sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value=
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()