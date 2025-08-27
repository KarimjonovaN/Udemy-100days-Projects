from selenium import webdriver
from selenium.webdriver.common.by import By

#keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver =  webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com")
# driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
#
# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value= "a-price-fraction")
# print(f"the price is {price_dollar.text}.{price_cents.text}")

driver.get("https://www.python.org/")
#
# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR,  value=".documentation-widget a")
# print(documentation_link.text)
#
# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

events = {}
upcoming_time = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
upcoming_events = driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")

for n in range(len(upcoming_time)):
    events[n]= {
        "time": upcoming_time[n].text,
        "name": upcoming_events[n].text
    }
print(events)

# driver.close() # loses the current active tab.
driver.quit()# quits the entire browser session.