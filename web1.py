
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#stopped at 0N__
driver = webdriver.Chrome()

driver.get('https://hash.hackthevalley.io/')


fil= open("output.txt","a")
f= open("dic.txt","r")
f1 = f.readlines()


for elem in f1:
    driver.find_element_by_xpath('//*[@id="inputHash"]').send_keys(elem+Keys.RETURN)
    output = driver.find_element_by_xpath('//*[@id="msg"]').text
    print(output)
    if (output != ''):
        #output = output[15:16]
        print(output)
        fil.write (output+"\n")
    driver.find_element_by_xpath('//*[@id="inputHash"]').clear()




