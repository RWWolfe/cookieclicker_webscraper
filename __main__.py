from selenium import webdriver
from xvfbwrapper import Xvfb
from scraper.cookie_scraper import CookieScraper
from scraper.scraper_strategy import Strategy
import time
from models.cookie_stats import CookieStats

vdisplay = Xvfb(width=1280, height=1280)

try:
    vdisplay.start()
    driver = webdriver.Chrome('/usr/bin/chromedriver/chromedriver')
    driver.get('http://orteil.dashnet.org/cookieclicker/')
    scraper = Strategy(driver=driver)
    
    run_name = input('Enter a run name: ')
    start = time.time()
    scraper.start_scrape()
    while not scraper.done:
        scraper.click_one_k()
        scraper.click_upgrade_ten()
        scraper.click_all_towers()
        scraper.check_done()
    end = time.time()
    run_time = (end - start)
    print(f'Run time: {run_time}')
    CookieStats.enter_new_run(run_name, run_time)

    
finally:
    driver.close()
    vdisplay.stop()
    





