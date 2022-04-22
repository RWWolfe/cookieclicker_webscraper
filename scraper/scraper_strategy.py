
from selenium.common.exceptions import StaleElementReferenceException

from scraper.cookie_scraper import CookieScraper


class Strategy(CookieScraper):
    def __init__ (self, driver, done = False):
        self.driver = driver
        self._done = done

    @property
    def done(self):
        return self._done

    @done.setter
    def done(self, bool):
        self._done = bool

    def start_scrape(self):
        self.click_stats()
        self.click_bulk_ten()
        self.click_cookie(500)
        self.click_cursor()
        self.click_upgrade(2)

    def click_one_k(self):
        self.click_cookie(1000)
        
    def click_five_k(self):
        self.click_cookie(5000)

    def click_upgrade_ten(self):
        try:
            self.click_upgrade(10)
        except StaleElementReferenceException:
            self.click_upgrade(10)

    def click_all_towers_ten(self):
        print('Buying 10 of all towers.')
        self.click_bulk_ten()
        self.click_factory()
        self.click_mine()
        self.click_farm()
        self.click_grandma()
        self.click_cursor()

    def click_all_towers(self):
        print('Buying 1 of all towers.')
        self.click_bulk_one()
        self.click_factory()
        self.click_mine()
        self.click_farm()
        self.click_grandma()
        self.click_cursor()

    
    
    def check_done(self):
        try:
            cookie_total = self.driver.find_element_by_xpath('//*[@id="menu"]/div[3]/div[4]/div')
            cookie_total_str = cookie_total.text.strip().replace(',', '').replace('\n', '')
            if 'million' in cookie_total_str:
                self.done = True
                return self.done
        except StaleElementReferenceException:
            cookie_total = self.driver.find_element_by_xpath('//*[@id="menu"]/div[3]/div[4]/div')
            cookie_total_str = cookie_total.text.strip().replace(',', '').replace('\n', '')
            if 'million' in cookie_total_str:
                self.done = True
                return self.done


    
