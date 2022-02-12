from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from routermanager.enumR import SecurityOptions

class OptionsElement:
    def __init__(self, element, classname, driver):
        self.driver = driver
        self.element = element
        self.options = WebDriverWait(element, 10).until(lambda d: d.find_elements(By.CLASS_NAME, classname))

    def listOptions(self):
        for i, op in enumerate(self.options):
            print(f"{i}: {op.find_element(By.CLASS_NAME, 'text').get_property('innerText')}")


class Security(OptionsElement):

    def __init__(self, driver, element):
        self.driver = driver
        OptionsElement.__init__(self, driver=driver, element=element, classname="ml2")
    def navigate(self, option):
        option = self.options[option.value]
        click = WebDriverWait(option, 10).until(lambda p: p.find_element(By.TAG_NAME, "a"))
        self.driver.execute_script("arguments[0].click();", click)
        #click = option.find_element(By.TAG_NAME, "a")
        click.click()
        #click =  WebDriverWait(option, 10).until(lambda p: p.find_element(By.CLASS_NAME, "content-container"))

    def accessControl(self, active=True):
        driver = self.driver
        self.navigate(SecurityOptions.ACCESS_CONTROL)
        container = WebDriverWait(driver, 10).until(lambda p: p.find_element(By.CLASS_NAME, "content-container"))
        buttonContainer = container.find_element(By.TAG_NAME, "div")
        buttonState = buttonContainer.get_property('className').split()
        buttonState = True if buttonState[2] == 'on' else False
        buttonClick = buttonContainer.find_element(By.CLASS_NAME, "button-group-wrap")

        if not (active == buttonState):
            buttonClick.click()
