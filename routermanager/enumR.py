from enum import Enum, unique


@unique
class AdvancedOptions(Enum):
    SECURITY = 7

class SecurityOptions(Enum):
    ACCESS_CONTROL = 2

class ModeEnum(Enum):
    ADVANCED = "advanced"
    BASIC = "basic"
    QUICKSTART = "qs"
