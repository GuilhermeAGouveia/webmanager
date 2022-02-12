from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


class ManagerWeb:
    def __init__(self, browser=Chrome):
        options = Options()
        options.headless = True
        self.driver = browser(options=options,
                              executable_path="/home/guilherme/Downloads/chromedriver_linux64/chromedriver")

    def close(self):
        self.driver.close()
