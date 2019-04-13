'''
Created on 11-Apr-2019

@author: Robin Singh
'''
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time
import screenshot
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

def signIn(testName):
    
    evidences = screenshot.takeEvidences(testName)
    # create a new Firefox session
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.maximize_window()
    
    # Navigate to the application home page
    driver.get("http://automationpractice.com/index.php")
    
    evidences.addEvidence('Home Page')
    
    signInButton = driver.find_element_by_xpath("/html/body/div[1]/div[1]/header/div[2]/div/div/nav/div[1]/a")
    signInButton.click()
    delay = 3 # seconds
    try:
        WebDriverWait(driver, delay).until(
                                   EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
        print ("Page is ready!")
    except TimeoutException:
        print ("Loading took too much time!")

    evidences.addEvidence('Sign In Screen')
    emailAdd = driver.find_element_by_xpath('//*[@id="email"]')
    actions = ActionChains(driver)
    actions.move_to_element(emailAdd).perform()
    emailAdd.send_keys('test@test.tst')
    
    pwd = driver.find_element_by_xpath('//*[@id="passwd"]')
    pwd.send_keys('test123')

    signInButton = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div/div/div[2]/form/div/p[2]/button/span')
    signInButton.click()
    evidences.addEvidence('Entered Credentials, now logging in.')
    time.sleep(3)
    
    evidences.addEvidence('Sign in Successful, Now, Signing out.')
    signOut = driver.find_element_by_xpath('/html/body/div[1]/div[1]/header/div[2]/div/div/nav/div[2]/a')
    signOut.click()
    # close the browser window
    evidences.addEvidence('Back to sign in page, Sign out successful')
    driver.quit()
