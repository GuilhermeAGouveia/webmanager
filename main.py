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
        raise Exception("Expected argument: active")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
