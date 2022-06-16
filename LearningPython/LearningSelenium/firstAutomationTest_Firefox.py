from selenium import webdriver

#driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver.exe")
driver = webdriver.Firefox()

driver.get("https://vltest.planetbids.com/home")
driver.maximize_window()
print(driver.title)
driver.close()