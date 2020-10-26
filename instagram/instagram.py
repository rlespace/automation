import os
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


browser = webdriver.Chrome(executable_path='path/to/chromedriver')

browser.get('https://www.instagram.com/')

sleep(3)
username_field = browser.find_element_by_name('username')
password_field = browser.find_element_by_name('password')

username_field.send_keys('USERNAME_GOES_HERE')
password_field.send_keys('PASSWORD_GOES_HERE')
sleep(1)
login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(2)
browser.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
sleep(1)
browser.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
sleep(5)

hashtags = ['architecture', 'building', 'city']
photos = []

for hashtag in hashtags:
    browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
    sleep(2)
    try:
        browser.find_element_by_xpath('//button[contains(text(), "Following")]')
    except NoSuchElementException:
        browser.find_element_by_xpath('//button[contains(text(), "Follow")]').click()
    finally:
        counter = 1
        elements = browser.find_elements_by_tag_name('a')
        for element in elements:
            href_attribute = element.get_attribute('href')
            if 'www.instagram.com/p' in href_attribute:
                if counter > 5: break
                photos.append(href_attribute)
                counter += 1
    sleep(1)

for photo in photos:
    browser.get(photo)
    sleep(2)
    try:
        browser.find_element_by_xpath('//span//*[local-name()="svg"][@aria-label="Unlike"]')
    except NoSuchElementException:
        browser.find_element_by_xpath('//span//*[local-name()="svg"][@aria-label="Like"]').click()
    finally:
        sleep(1)

sleep(3)
browser.close()
