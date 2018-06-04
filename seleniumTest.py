from selenium import webdriver
from selenium.webdriver.common.keys import Keys

DRIVER_EXE = r"C:\Users\Andrew Yan\Documents\GitHub\data_skills\geckodriver.exe"

#the instance of Firefox WebDriver is created.
driver = webdriver.Firefox(executable_path=DRIVER_EXE) 

#The driver.get method will navigate to a page given by the URL. 
driver.get("http://www.python.org")

#The next line is an assertion to confirm that title has “Python” word in it:
assert "Python" in driver.title

#WebDriver offers a number of ways to find elements using one of the find_element_by_* methods. 
#"find_element_by_* methods" return a list of all WebElements, or an empty list if nothing matches
elem = driver.find_element_by_name("q")
#??? What is stored in elem now? 
'''
Next, we are sending keys, this is similar to entering keys using your keyboard. 
Special keys can be sent using Keys class imported from selenium.webdriver.common.keys.
To be safe, we’ll first clear any pre-populated text in the input field (e.g. “Search”) 
so it doesn’t affect our search results:
'''
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()