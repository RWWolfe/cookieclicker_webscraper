### this is not implemented

"""
from selenium import webdriver
from xvfbwrapper import Xvfb


vdisplay = Xvfb()

try:
    vdisplay.start()
    driver = webdriver.Chrome('/usr/bin/chromedriver/chromedriver')

finally:
    vdisplay.stop()
    driver.close()
"""