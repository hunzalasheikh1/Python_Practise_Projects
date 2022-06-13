from lib2to3.pgen2 import driver
import booking.constants as const

#only for windows
import os
from selenium import webdriver


class Booking(webdriver.Chrome):
    def __init__(self,driver_path=r"chromedriver.exe",teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking,self).__init__()
        
    def land_first_page(self):
        self.get(const.BASE_URL)
        
        
