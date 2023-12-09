import logging
import sys


class ConfigManager:

    def __init__(self):
        self.conversionType = None
        self.lispNameFile = None
        self.directory = None

    def main(self):
        self.loadConfigFile()

    def loadConfigFile(self):
        f = open("resources/Config.txt", "r")

        for i in f:
            if i.startswith("-"):
                s = i.split("=")[0]
                s1 = i.split("=")[1]

                print(s1)

                if str(s1).startswith("0"):
                    logging.error("Please configure the configuration file")
                    sys.exit()

                if s == "- conversion ":
                    self.conversionType = s1

                if s == "- lispName ":
                    self.lispNameFile = s1

                if s == "- directoryName ":
                    self.directory = s1

    def getConversionType(self) -> int:
        return self.conversionType

    def getLispNameFile(self) -> str:
        return str(self.lispNameFile)

    def getDirectory(self) -> str:
        return str(self.directory)