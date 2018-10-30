from selenium import webdriver

options = webdriver.ChromeOptions()
options.binary_location = '/usr/bin/google-chrome-stable'
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://twitter.com/login')

userfield = driver.find_element_by_css_selector('.js-username-field.email-input.js-initial-focus')
userfield.send_keys('chirag3')

passwordfield = driver.find_element_by_css_selector('.js-password-field')
passwordfield.send_keys('hunter2')

passwordfield.submit()

driver.get('https://twitter.com/chirag3/following')
driver.execute_script("window.scrollTo(0, 10000);")
driver.get_screenshot_as_file('followers-page.png')

driver.quit()