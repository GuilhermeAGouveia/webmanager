from dotenv import load_dotenv
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

load_dotenv()
path = os.getenv("WEBDRIVER_PATH")

class ManagerWeb:
    def __init__(self, browser=Chrome):
        options = Options()
        options.headless = True
        self.driver = browser(options=options,
                              executable_path=path)

    def close(self):
        self.driver.close()
