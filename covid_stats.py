from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    path = "/Users/DuarteCasaleiro/Developer/Program_files/chromedriver"
    driver = webdriver.Chrome(path)

    url = "https://www.google.com/search?q=covid&oq=covid&aqs=chrome..69i57j69i59j69i60l2.1864j0j7&sourceid=chrome&ie=UTF-8"
    driver.get(url)
    # driver.quit()
    driver.implicitly_wait(5)
    accept_terms = driver.find_element(By.ID, "L2AGLb")
    actions = ActionChains(driver)
    actions.click(accept_terms)
    actions.perform()

    news = driver.find_element(By.CLASS_NAME, "UcHR6e")
    actions.click(news)
    actions.perform()




