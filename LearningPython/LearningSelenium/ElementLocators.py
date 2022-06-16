from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class  DemoFindElementByID():

    def locate_by_id_demo(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://vltest.planetbids.com/home")



