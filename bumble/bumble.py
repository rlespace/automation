
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://bumble.com/get-started')
driver.maximize_window()
sleep(3)
# sign in using facebook
continue_with_fb_button = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[1]/div/div[2]/div')
continue_with_fb_button.click()
sleep(1)

bumble_window = driver.window_handles[0]
popup_window = driver.window_handles[1]

# switch back to facebook popup window
driver.switch_to.window(popup_window)

email_field = driver.find_element_by_xpath('//*[@id="email"]')
email_field.send_keys('YOUR_USERNAME_GOES_HERE')

password_field = driver.find_element_by_xpath('//*[@id="pass"]')
password_field.send_keys('YOUR_PASSWORD_GOES_HERE')

login_button = driver.find_element_by_xpath('//*[@id="u_0_0"]')
login_button.click()
sleep(2)

# switch back to bumble window
driver.switch_to.window(bumble_window)
sleep(5)

def swipe_right(wait=5):
    like_button = driver.find_element_by_xpath(
        '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span'
    )
    like_button.click()
    sleep(wait)

def swipe_left(wait=5):
    dislike_button = driver.find_element_by_xpath(
        '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/div[1]/span'
    )
    dislike_button.click()
    sleep(wait)

def close_popup(wait=5):
    continue_with_bumble_button = driver.find_element_by_xpath(
        '//*[@id="main"]/div/div[1]/main/div[2]/article/div/footer/div[2]/div[2]/div/span/span/span/span'
    )
    continue_with_bumble_button.click()
    sleep(wait)

def open_chat(wait=5):
    open_chat_button = driver.find_element_by_xpath(
        '//*[@id="main"]/div/div[1]/main/div[2]/article/div/footer/div[2]/div[1]/div'
    )
    open_chat_button.click()
    sleep(wait)


single = True
while single:
    try:
        swipe_right()
    except Exception:
        open_chat()
        single = False

driver.close()
