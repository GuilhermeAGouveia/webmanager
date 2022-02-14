import os
from dotenv import load_dotenv

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from routermanager.enumR import SecurityOptions

load_dotenv()
time_out = int(os.getenv("TIME_OUT"))


class OptionsElement:
    def __init__(self, element, classname, driver):
        self.driver = driver
        self.element = element
        self.options = WebDriverWait(element, time_out).until(lambda d: d.find_elements(By.CLASS_NAME, classname))

    def listOptions(self):
        for i, op in enumerate(self.options):
            print(f"{i}: {op.find_element(By.CLASS_NAME, 'text').get_property('innerText')}")


class Security(OptionsElement):

    def __init__(self, driver, element):
        self.driver = driver
        OptionsElement.__init__(self, driver=driver, element=element, classname="ml2")

    def navigate(self, option):
        option = self.options[option.value]
        click = WebDriverWait(option, time_out).until(lambda p: p.find_element(By.TAG_NAME, "a"))
        self.driver.execute_script("arguments[0].click();", click)

    def accessControl(self):
        self.navigate(SecurityOptions.ACCESS_CONTROL)
        return AccessControll(self.driver)


class AccessControll:
    def __init__(self, driver):
        self.driver = driver
    def active(self, active=False):
        container = WebDriverWait(self.driver, time_out).until(lambda p: p.find_element(By.CLASS_NAME, "content-container"))
        buttonContainer = container.find_element(By.TAG_NAME, "div")
        buttonState = buttonContainer.get_property('className').split()
        buttonState = True if buttonState[2] == 'on' else False
        buttonClick = buttonContainer.find_element(By.CLASS_NAME, "button-group-wrap")
        if not (active == buttonState):
            print("Block active" if active else "Block disable")
            buttonClick.click()
        else:
            print("Block option already")

        return True