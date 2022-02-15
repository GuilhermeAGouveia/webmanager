import os
from dotenv import load_dotenv
from pprint import pprint
from routermanager.main import RouterManager
from routermanager.enumR import ModeEnum

load_dotenv()

gw_addr = os.getenv("GATEWAY_ADDRESS")


def testBlackList():
    rm = RouterManager(url=f"http://{gw_addr}")
    rm.login()
    advanced = rm.alterMode(ModeEnum.ADVANCED)
    security = advanced.security()
    accessControl = security.accessControl()
    pprint(accessControl.blackList)
    rm.close()

testBlackList()