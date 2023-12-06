import logging
import os
import sys


class FileManager:

    # conversionType : 0 = none; 1 = to Literal; 2 = to ladder
    def __init__(self, lispNameFile, directory, conversionType):
        self.lispNameFile = lispNameFile
        self.directory = directory
        self.conversionType = int(conversionType)
        self.lispPath = self.directory + self.lispNameFile
        self.literalPath = self.directory + "LispLiteral"
        self.ladderPath = self.directory + "Ladder"
        self.lispRead = None
        self.literalWrite = None
        self.ladderWrite = None

    def start(self):

        if not self.getFileExist():
            logging.error("Lisp File not find; disable program")
            sys.exit()

        else:
            self.createLiteralFile()
            self.createLadderFile()

            self.getReadLispFile()

            if self.conversionType == 1:
                self.getWriteLiteralFile()

            elif self.conversionType == 2:
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
