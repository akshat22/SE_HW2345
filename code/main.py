from code.Cli import *
from code import config
from code import LuaPythonTestEngine


if __name__ == '__main__':
    cliObject = Cli()
    the = cliObject.cli(cliObject.the)
    config.baseSettings = the

    if the["eg"] != "nothing":
        LuaPythonTestEngine.runs(the["eg"])
