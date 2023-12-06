import logging
import sys

from converter.FileManager import FileManager
from converter.ConfigManager import ConfigManager

memoryStorage = {}


def main():

    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)
    logging.info("Converter enable")

    memory("config", ConfigManager())
    memory("config").main()

    memory("FileManager", FileManager(memory("config").getLispNameFile(), memory("config").getDirectory(),
                                      memory("config").getConversionType()))
    memory("FileManager").start()


def printMemory():
    print("--------------MEMORY:-------------------")
    for k, v in memoryStorage.items():
        print("Nom : ", k, " Valeur :", v, " Type : ", type(v))
    print("----------------------------------------")
    print("\n")


def memory(key: object, value: object = None) -> object:
    global memoryStorage
    if " " in key:
        logging.error("Prohibited space in variable names: " + key + "\n")
        sys.exit()
    if value is not None:
        memoryStorage[key] = value
    else:
        try:
            return memoryStorage[key]
        except:
            logging.error("Unknown variable name: " + key)
            sys.exit()


if __name__ == "__main__":
    main()
