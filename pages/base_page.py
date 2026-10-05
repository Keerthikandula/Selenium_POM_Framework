from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout= 10) # You can adjust the timeout as needed
        

    def open(self, url: str):
        self.driver.get(url)
        

    def find(self, locator: tuple):
        return self.wait.until(EC.element_to_be_clickable(locator)) 
        

    def click(self, locator: tuple):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator: tuple, text: str):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)
        
    
    def text_of(self, locator: tuple) -> str:
        return self.find(locator).text.strip()
        
    
    def is_visible(self, locator: tuple) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False