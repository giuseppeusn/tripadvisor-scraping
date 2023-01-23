import colorama
colorama.init(wrap=True)

class bcolors:
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'


def loading(msg):
    return f"{bcolors.UNDERLINE}{bcolors.OKCYAN}{msg}\n{bcolors.ENDC}"


def fail(msg):
    return f"{bcolors.FAIL}{msg}\n{bcolors.ENDC}"


def success(msg):
    return f"{bcolors.OKGREEN}{msg}\n{bcolors.ENDC}"