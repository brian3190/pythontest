from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.seleniumeasy.com/test/basci-first-form-demo.html')
messageField = driver.find_elemen_by_xpath('//*[@id=üser-message"]')
messageField.send_keys('Hello World')
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()
additionField1 = driver.find_element_by_xpath('//*[@id="sum1"]')
additionField1.send_keys('10')
additionField2 = driver.find_element_by_xpath('//*[@id="sum2"]')
additionField2.send_keys('11')
getTotalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
getTotalButton.click()