from routermanager.enumR import AdvancedOptions
from routermanager.options import *


class Mode(OptionsElement):

    def __init__(self, driver):
        OptionsElement.__init__(self, driver=driver, element=driver, classname="ml1")


class AdvancedMode(Mode):

    def __init__(self, driver):
        Mode.__init__(self, driver=driver)

        # while True:
        #     options = driver.find_elements(By.CLASS_NAME, "ml")
        #     if len(options) > 0:
        #         break
        #     else:
        #         continue
        # self.options = options

    def security(self):
        driver = self.driver
        security = self.options[AdvancedOptions.SECURITY.value]
        security.click()
        return Security(driver=driver, element=security)
