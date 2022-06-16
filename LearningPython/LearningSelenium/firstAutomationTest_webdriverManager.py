from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

#from webdriver_manager.firefox import GeckoDriverManager
#driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

#from webdriver_manager.microsoft import EdgeChromiumDriverManager
#driver = webdriver.Edge(EdgeChromiumDriverManager().install())

driver.get("https://vltest.planetbids.com/home")
driver.maximize_window()
print(driver.title)
driver.close()