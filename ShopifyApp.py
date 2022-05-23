#from decouple import config
import click
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
from requests import Session
import sys
from retry import retry
from Date import Date_
from selenium.common.exceptions import (
    ElementNotInteractableException,
    StaleElementReferenceException,
    ElementClickInterceptedException,
    ElementNotVisibleException,
)
from RPA.Robocorp.Vault import Vault

secret= Vault().get_secret("Config")

class Shopify:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable-automation"])
        self.driver = webdriver.Chrome(executable_path=r"chromedriver.exe", chrome_options=options)
    def open_login_window(self):
        website="https://accounts.shopify.com/lookup?rid=05dc5f57-2da6-45ad-9fc8-a172078a9a9e"
        self.driver.get("https://partners.shopify.com/organizations")
        #driver = webdriver.Chrome(ChromeDriverManager().install())
    @retry((ElementNotInteractableException,ElementNotVisibleException,ElementClickInterceptedException),3,3)
    def submit(self):
        submit = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, 'commit')))
        submit.click()
    def login(self):
        self.username=secret['Loginid']
        self.password=secret['password']
        self.driver.refresh()
        self.driver.find_element_by_id("account_email").send_keys(self.username)
        self.submit()
        print("entered email id")
        self.driver.switch_to.frame(0)
        print("switched frame")
        time.sleep(3)
        self.driver.find_element_by_id("account_password").send_keys(self.password)
        self.submit()
        self.driver.switch_to.default_content()
        return
    
    @retry((ElementNotInteractableException,ElementNotVisibleException,ElementClickInterceptedException),3,3)
    def click_link(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT,"PicAmaze Animate Images, Gifs"))).click()
        #self.driver.find_element_by_class_name("FeTD8").click()
        time.sleep(5)
    def view_history(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT,"View all history"))).click()

    def get_email(self):
        time.sleep(5)
        print("in get_email.....")
        rows = self.driver.find_elements_by_xpath("//table/tbody/tr")
        list_activity={}
        list_activity['Closed Store']=[]
        list_activity['Uninstalled']=[]
        list_activity['Installed']=[]
        list_activity['Uninstalled']=[]
        list_activity['Recurring charge cancelled']=[]
        list_activity['Recurring charge activated']=[ ]
        # Iterate over the rows
        finish=False
        temps=[]
        for row in rows:
            # Get all the columns for each row. 
            # cols = row.find_elements_by_xpath("./*")
            cols = row.find_elements_by_xpath("./*[name()='th' or name()='td']")
            temp = [] # Temproary list
            for col in cols:
                temp.append(col.text)
            print(temp)
            temps.append(temp)
        print("newline",temps,sep='\n')  
        for r in temps:
            date_inword=r[0]
            date_=Date_(date_inword)
            date_.convert_date_in_numbers()
            if date_.match_date() == True:
                activity=r[2].split('\n')[1]
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT,r[1]))).click()
                element=self.driver.find_element_by_xpath('//*[@id="AppFrameMain"]/div/div/div[2]/div/section[1]/div[3]/p[1]/a')
                list_activity[activity].append(element.text)
                self.driver.execute_script("window.history.go(-1)")
                time.sleep(1)
            else:
                finish=True
                break 
        return list_activity
        
    def open_workplace(self):
        self.driver.find_element_by_xpath("//span[contains(text(),'Propero')]").click()
        time.sleep(5)
        self.click_link()
        self.view_history()
        email_pair=self.get_email()
        return email_pair
   
