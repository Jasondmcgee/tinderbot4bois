import time
from selenium import webdriver
import json
from time import sleep

phone = 6507015258

class TinderBot:
    def __init__(self, phone):
        self.chrome_options =  webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(
            executable_path=r"chromedriver/chromedriver.exe",
            chrome_options=self.chrome_options)
        self.driver.get("https://tinder.com/")
        sleep(4)
        self.driver.find_element_by_xpath('//*[contains(text(), "Log in with phone number")]').click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div[2]/div/input').send_keys(phone)
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button/span').click()
        self.type_phone_code()

    def type_phone_code(self):
        phone_code = input("type the code in here")
        sleep(1)
        self.driver.find_element_by_xpath('//*[@aria-describedby="codeVerificationErrorMessage"]/input[1]').send_keys(phone_code)
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button[2]').click()

tinder = TinderBot(phone)