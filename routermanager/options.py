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
        # click = WebDriverWait(option, time_out).until(lambda p: p.find_element(By.TAG_NAME, "a"))
        click = option.find_element(By.TAG_NAME, "a")
        self.driver.execute_script("arguments[0].click();", click)

    def accessControl(self):
        self.navigate(SecurityOptions.ACCESS_CONTROL)
        return AccessControll(self.driver)


class AccessControll:
    def __init__(self, driver):
        self.driver = driver
        self.blackList = self.getBlackList()

    def active(self, active=False):
        container = WebDriverWait(self.driver, time_out).until(
            lambda p: p.find_element(By.CLASS_NAME, "content-container"))

        def getState(buttonContainer):
            buttonState = buttonContainer.get_property('className').split()
            buttonState = True if buttonState[2] == 'on' else False
            return buttonState

        buttonContainer = container.find_element(By.TAG_NAME, "div")
        buttonClick = buttonContainer.find_element(By.CLASS_NAME, "button-group-cover")
        if not (active == getState(buttonContainer)):
            print("Block active" if active else "Block disable")
            self.driver.execute_script("arguments[0].click();", buttonClick)

        else:
            print("Block option already")

        return True

    def getBlackList(self):
        bodyTable = WebDriverWait(self.driver, time_out).until(
            lambda p: p.find_element(By.ID, "bodyDevicesInBlackList"))
        listTr = bodyTable.find_elements(By.TAG_NAME, "tr")[1:]
        listDevices = []
        for elem in listTr:
            elem = elem.find_elements(By.TAG_NAME, "td")[1:]
            arrayDict = {
                "id": int(elem[0].get_property("innerText")),
                "name": elem[1].get_property("innerText"),
                "mac": elem[2].get_property("innerText"),
                "actions": elem[3].find_elements(By.TAG_NAME, "span")
            }
            listDevices.append(arrayDict)
        return listDevices
