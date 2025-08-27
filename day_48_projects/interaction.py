from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver =  webdriver.Chrome(chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Using click method with BY_CSS_SELECTOR
# particular_num = driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# particular_num.click()
# print(particular_num.text)

# Using click method with BY.LINK_TEXT
# all_portals= driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the 'search' <input> by Name.
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

fname = driver.find_element(By.NAME, value= "fName")
fname.send_keys("Navruza")
lname = driver.find_element(By.NAME, value="lName")
lname.send_keys("Karimjonova")
email_address = driver.find_element(By.NAME, value="email")
email_address.send_keys("ruby.wilson.0911@gmail.com")
sign_up = driver.find_element(By.CSS_SELECTOR, value="form button")
sign_up.send_keys(Keys.ENTER)







# what is the difference between the find.elements and find.element?
# and when I used the find_elements in printing section text method did  ot worked