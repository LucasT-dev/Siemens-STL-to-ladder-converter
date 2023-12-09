import logging
import os
import sys
import time


class FileManager:

    # conversionType : 0 = none; 1 = to Literal; 2 = to ladder
    def __init__(self, lispNameFile, directory, conversionType):

        self.named_tuple = time.localtime()  # get struct_time
        self.time_string = time.strftime(" %Y_%m_%d %H_%M_%S ", self.named_tuple)

        self.lispNameFile = lispNameFile
        self.directory = directory
        self.conversionType = int(conversionType)
        self.lispPath = self.directory + self.lispNameFile
        self.literalPath = self.directory + "LispLiteral" + self.time_string + ".txt"
        self.ladderPath = self.directory + "Ladder" + self.time_string + ".txt"
        self.lispRead = None
        self.literalWrite = None
        self.ladderWrite = None

        logging.debug("File date :" + self.time_string)

    def start(self):

        self.lispPath = self.lispPath.replace("\n", "")
        self.literalPath = self.literalPath.replace("\n", "")
        self.ladderPath = self.ladderPath.replace("\n", "")

        if not self.getFileExist():
            logging.error("Lisp File not find; disable program")
            sys.exit()

        else:

            self.getReadLispFile()

            if self.conversionType == 1:
                self.createLiteralFile()
                self.getWriteLiteralFile()

            elif self.conversionType == 2:
                self.createLadderFile()
                self.getWriteLadderFile()

            else:
                logging.error("Conversion type unknown ")

        print("Succes")

    def getFileExist(self) -> bool:
        return os.path.isfile(self.lispPath)

    def createLiteralFile(self):
        self.literalWrite = open(self.literalPath, "x")

    def createLadderFile(self):
        self.ladderWrite = open(self.ladderPath, "x")

    def closeAllFile(self):
        self.lispRead.close()
        self.ladderWrite.close()
        self.literalWrite.close()

    def getReadLispFile(self):
        return self.lispRead

    def getWriteLiteralFile(self):
        return self.literalWrite

    def getWriteLadderFile(self):
        return self.ladderWrite
