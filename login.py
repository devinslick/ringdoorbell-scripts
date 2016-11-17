from selenium import webdriver
driver=webdriver.Chrome('/opt/seleniumdrivers/chromedriver')
driver.get("https://ring.com/users/sign_in")
username = driver.find_element_by_id("user_email")
password = driver.find_element_by_id("user_password")
username.send_keys("myemail@address.com")
password.send_keys("myringPassword")
username.submit()
driver.get("https://ring.com/account/activity")
URL = driver.find_element_by_tag_name('a').get_attribute('href')
print URL
html_source = driver.page_source
print html_source
