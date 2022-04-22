from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
#from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
import time





class CookieScraper:
    def __init__(self, driver):
        self.driver = driver
        

    def click_stats(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@id="statsButton"]'))
            )
        except TimeoutException:
            print("Failed to click: Stats")
        try:
            stats = self.driver.find_element_by_xpath("//div[@id='statsButton']")
            stats.click()
        except StaleElementReferenceException:
            stats = self.driver.find_element_by_xpath("//div[@id='statsButton']")
            stats.click()

    def click_bulk_ten(self):
        bulk_ten = self.driver.find_element_by_xpath("//div[@id='storeBulk10']")
        bulk_ten.click()
    
    def click_bulk_one(self):
        bulk_one = self.driver.find_element_by_xpath("//div[@id='storeBulk1']")
        bulk_one.click()

    def click_upgrade(self, upgrades):
        try:
            for i in range(0, upgrades):
                upgrade = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[19]/div[3]/div[5]/div[1]")
                upgrade.click()
                time.sleep(.1)
            print(f'Clicking {upgrades} upgrades.')
        except (ElementNotInteractableException, NoSuchElementException):
            pass

    def click_cookie(self, cookies):
        try:
            WebDriverWait(self.driver, 0).until(
                EC.presence_of_element_located((By.XPATH, '//div[@id="bigCookie"]'))
            )
        except TimeoutException:
            print("Failed to click: Cookie")
        cookie_el = self.driver.find_element_by_xpath("//div[@id='bigCookie']")
        
        for i in range(0, cookies):
            cookie_el.click()
            if i % 50 == 0:
                try:
                    cookie_total = self.driver.find_element_by_xpath('//*[@id="menu"]/div[3]/div[4]/div')
                    cookie_total_str = cookie_total.text.strip().replace(',', '').replace('\n', '')
                    print(f'Clicking cookies. Total cookies: {cookie_total_str}')
                except StaleElementReferenceException:
                    cookie_total = self.driver.find_element_by_xpath('//*[@id="menu"]/div[3]/div[4]/div')
                    cookie_total_str = cookie_total.text.strip().replace(',', '').replace('\n', '')
                    print(f'Clicking cookies. Total cookies: {cookie_total_str}')
                try:
                    golden_cookie_el = self.driver.find_element_by_xpath("//div[@class='shimmer']")
                    golden_cookie_el.click()
                except (ElementNotInteractableException, StaleElementReferenceException, NoSuchElementException):
                    pass


    def click_cursor(self):
        try:
            WebDriverWait(self.driver, 0).until(
                EC.presence_of_element_located((By.XPATH, '//div[@id="product0"]'))
            )
        except TimeoutException:
            print("Failed to click: Cursor")
        try:
            cursor_el = self.driver.find_element_by_xpath("//div[@id='product0']")
            cursor_el.click()
        except ElementNotInteractableException:
            pass
            
    
    
    def click_grandma(self):
        try:
            WebDriverWait(self.driver, 0).until(
                EC.presence_of_element_located((By.XPATH, '//div[@id="product1"]'))
            )
        except TimeoutException:
            print("Failed to click: Grandma")
        try:
            grandma_el = self.driver.find_element_by_xpath("//div[@id='product1']")
            grandma_el.click()
        except ElementNotInteractableException:
            pass

    def click_farm(self):
        try:
            WebDriverWait(self.driver, 0).until(
                EC.presence_of_element_located((By.XPATH, '//div[@id="product2"]'))
            )
        except TimeoutException:
            print("Failed to click: Farm")
        try:
            farm_el = self.driver.find_element_by_xpath("//div[@id='product2']")
            farm_el.click()
        except ElementNotInteractableException:
            pass

    def click_mine(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@id="product3"]'))
            )
        except TimeoutException:
            print("Failed to click: Mine")
        try:
            mine_el = self.driver.find_element_by_xpath("//div[@id='product3']")
            mine_el.click()
        except ElementNotInteractableException:
            pass

    def click_factory(self):
        try:
            WebDriverWait(self.driver, 0).until(
                EC.presence_of_element_located((By.XPATH, '//div[@id="product4"]'))
            )
        except TimeoutException:
            print("Failed to click: Factory")
        try:
            factory_el = self.driver.find_element_by_xpath("//div[@id='product4']")
            factory_el.click()
        except ElementNotInteractableException:
            pass


    ### Not needed to reach 1 million
    #def click_bank(self):
    #    try:
    #        WebDriverWait(self.driver, 0).until(
    #            EC.presence_of_element_located((By.XPATH, '//div[@id="product5"]'))
    #        )
    #    except TimeoutException:
    #        print("Failed to click: Bank")
    #    try:
    #        bank_el = self.driver.find_element_by_xpath("//div[@id='product5']")
    #        bank_el.click()
    #    except ElementNotInteractableException:
    #        pass






# //span[@id='productPrice0']
# except ElementClickInterceptedException: