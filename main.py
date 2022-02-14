import warnings

from dotenv import load_dotenv
from routermanager.enumR import ModeEnum
from routermanager.main import RouterManager
import sys
import os

load_dotenv()

gw_addr = os.getenv("GATEWAY_ADDRESS")

def blockMotherPhone(active):
    rm = RouterManager(url=f"http://{gw_addr}")
    rm.login()
    advanced = rm.alterMode(ModeEnum.ADVANCED)
    security = advanced.security()
    access_control = security.accessControl()
    access_control.active(active)
    rm.close()


if __name__ == '__main__':
    try:
        blockMotherPhone(True if sys.argv[1].lower() == '-a' else False)
    except IndexError:
        warnings.warn("\033[93m [WARNING] A flag -a or -f não foi indicada, na ausência, -f sera considerado! \033[0m")
        blockMotherPhone(False)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
