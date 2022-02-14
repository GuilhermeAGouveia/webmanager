from dotenv import load_dotenv
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import os

from routermanager.enumR import ModeEnum
from manager import ManagerWeb
from routermanager.mode import *

load_dotenv()
time_out = int(os.getenv("TIME_OUT"))

class RouterManager(ManagerWeb):
    def __init__(self, url):
        ManagerWeb.__init__(self, browser=Chrome)
        self.url = url
        self.state = {
            "login": False
        }

    def login(self):
        driver = self.driver
        driver.get(self.url)
        password = driver.find_element(By.ID, "pc-login-password")
        password.send_keys("admin", Keys.ENTER)
        try:
            alert = driver.find_element(By.ID, "alert-container")
            alert.find_element(By.ID, "confirm-yes").click()
            print("Forçando login")

        except:
            pass
        self.state = {
            "login": True
        }

    def alterMode(self, mode):
        assert self.state["login"]
        driver = self.driver
        if mode == ModeEnum.ADVANCED:
            mode = WebDriverWait(driver, time_out).until(lambda p: p.find_element(By.ID, ModeEnum.ADVANCED.value))
            mode.click()
            return AdvancedMode(driver=self.driver)
        elif mode == ModeEnum.BASIC:
            raise Exception("Sorry, function unsupported")
        else:
            raise Exception("Sorry, function unsupported")

    def close(self):
        assert self.state["login"]
        driver = self.driver
        driver.find_element(By.ID, "topLogout").click()
        alert = driver.find_element(By.ID, "alert-container")
        buttons = alert.find_elements(By.TAG_NAME, "button")
        buttons[1].click()  # Clica em sim para confirmar logout
        ManagerWeb.close(self)


if __name__ == '__main__':
    print("Não disponivel")
