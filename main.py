import random
import warnings
import time

from dotenv import load_dotenv
from routermanager.enumR import ModeEnum
from routermanager.main import RouterManager
import sys
import os

load_dotenv()

gw_addr = os.getenv("GATEWAY_ADDRESS")

"""
    Bloqueio e desbroqueio imediato
    :param active :type bool indica se devemos bloquear (True) ou desbloquear (False)
"""


def blockMotherPhone(active):
    rm = RouterManager(url=f"http://{gw_addr}")
    rm.login()
    advanced = rm.alterMode(ModeEnum.ADVANCED)
    security = advanced.security()
    access_control = security.accessControl()
    access_control.active(active)
    rm.close()


"""
    Bloqueia e desbroqueia conexão com roteador, causando sensação de rede instável
    :param  finalState indica se ao final a conexão é bloqueada (-a), ou desbloquada (-f) [DEFAULT]
    :param n_interations indica o numero de iterações entre desbloquear e bloquear
"""


def blockMotherPhoneTimer(finalState: str = "-f", n_interations: int = 10) -> None:
    print("Block timer started!")
    rm = RouterManager(url=f"http://{gw_addr}")
    rm.login()
    advanced = rm.alterMode(ModeEnum.ADVANCED)
    security = advanced.security()
    access_control = security.accessControl()
    toggle = False
    for i in range(0, n_interations):
        print(f"Block sequence {i}:")
        toggle = not toggle
        access_control.block(toggle)
        """
        O router parece levar mais tempo para bloquear conexão do que para desbloquear,
        a condicional abaixo serve para tratar isso, após o desbloqueio, o tempo para bloquear é menor
        """
        if toggle:
            time_wait = random.randrange(6, 10) #Depois de bloquear, leva de 6 a 10 segundos para desbloquear
        else:
            time_wait = random.randrange(2, 4) #Depois de desbloquear, leva de 2 a 4 segundos para bloquear
        time.sleep(time_wait)

    if finalState == "-a":
        access_control.block(True)
    else:
        access_control.block(False)

    rm.close()


if __name__ == '__main__':
    try:
        if sys.argv[1].lower() == '-t':
            try:
                blockMotherPhoneTimer(n_interations=int(sys.argv[2]), finalState=sys.argv[3].lower())
            except IndexError:
                blockMotherPhoneTimer()
        else:
            blockMotherPhone(True if sys.argv[1].lower() == '-a' else False)

    except IndexError:
        warnings.warn("\033[93m [WARNING] A flag -a or -f não foi indicada, na ausência, -f sera considerado! \033[0m")
        blockMotherPhone(False)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
