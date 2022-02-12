# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from routermanager.enumR import ModeEnum
from routermanager.main import RouterManager
import sys


def blockMotherPhone(active):
    rm = RouterManager(url="http://192.168.0.1")
    rm.login()
    advanced = rm.alterMode(ModeEnum.ADVANCED)
    security = advanced.security()
    security.listOptions()
    security.accessControl(active)
    rm.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    blockMotherPhone(bool(sys.argv[0]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
