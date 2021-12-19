from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

path = "/Users/DuarteCasaleiro/Developer/Program_files/chromedriver"
driver = webdriver.Chrome(path)

url = "https://www.google.com/search?q=covid&oq=covid&aqs=chrome..69i57j69i59j69i60l2.1864j0j7&sourceid=chrome&ie=UTF-8"
driver.get(url)

# accept google terms and conditions
driver.implicitly_wait(5)
accept_terms = driver.find_element(By.ID, "L2AGLb")
actions = ActionChains(driver)
actions.click(accept_terms)
actions.perform()

# google news covid-19 page
news = driver.find_element(By.CLASS_NAME, "UcHR6e")
actions.click(news)
actions.perform()
driver.implicitly_wait(5)

total_stats = driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[2]/div[2]/div[4]/div/div/div[1]/"
                                            "div[1]/div[1]/div/div[1]/div[2]").text

new_cases = driver.find_element(By.XPATH,
                                "//*[@id='yDmH0d']/c-wiz/div/div[2]/div[2]/div[4]/div/div/div[1]/div[1]/div[1]"
                                "/div/div[1]/div[3]/strong").text
per_milion_cases = driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[2]/div[2]/div[4]/div/div/div"
                                                 "[2]/div/div[2]/table/tbody/tr[2]/td[4]").text

total_deaths = driver.find_element(By.XPATH,
                                   "//*[@id='yDmH0d']/c-wiz/div/div[2]/div[2]/div[4]/div/div/div[1]/div[1]/"
                                   "div[1]/div/div[3]/div[2]").text
new_deaths = driver.find_element(By.XPATH,
                                 "//*[@id='yDmH0d']/c-wiz/div/div[2]/div[2]/div[4]/div/div/div[1]/div[1]/"
                                 "div[1]/div/div[3]/div[3]/strong").text

total_doses = driver.find_element(By.XPATH,
                                  "//*[@id='yDmH0d']/c-wiz/div/div[2]/div[2]/div[4]/div/div/div[1]/div[1]/"
                                  "div[3]/div/div[1]/div[2]").text

total = [total_stats, new_cases, per_milion_cases, total_deaths, total_doses]

f = open("database.txt", "w")
for n in range(len(total)):
    f.write(total[n] + "\n")
f.close()

driver.quit()



