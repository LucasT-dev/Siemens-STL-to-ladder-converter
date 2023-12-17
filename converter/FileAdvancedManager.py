import logging
import string


class FileAdvancedManager:

    def __init__(self, pathFile: string):

        self.pathFile = pathFile
        self.write = None
        self.read = None

    def __writeFile(self):
        self.write = open(self.pathFile, "w")

    def __readFile(self):
        self.read = open(self.pathFile, "r")

    def __closeWriteFile(self):
        self.write.close()

    def __closeReadFile(self):
        self.read.close()

    def readAllLine(self) -> string:

        # Open a file in reading mode to read its contents
        with open(self.pathFile, 'r') as filer:
            lines = filer.readlines()

        result = ""

        for index, line in enumerate(lines):
            result = result + line.strip() + "\n"

        return result

    def readLine(self, at: int) -> string:

        # Open a file in reading mode to read its contents
        with open(self.pathFile, 'r') as filer:
            lines = filer.readlines()

        if at > len(lines):
            logging.error("Invalid index, beyond file size")

            return "None"

        return lines[at]

    def getLengthLine(self, line: int) -> int:

        return len(self.readLine(line))

    def insertAt(self, index: int, text: string):

        # Open a file in reading mode to read its contents
        with open(self.pathFile, 'r') as filer:
            lines = filer.readlines()

        # Insert text at specified index
        lines.insert(index, text + "\n")

        # Rewrite the entire contents of the file with the new line inserted
        with open(self.pathFile, 'w') as filew:
            filew.writelines(lines)

    def insertReturnLineAt(self, index: int):

        # Open a file in reading mode to read its contents
        with open(self.pathFile, 'r') as filer:
            lines = filer.readlines()

        # Insert text at specified index
        lines.insert(index, "\n")

        # Rewrite the entire contents of the file with the new line inserted
        with open(self.pathFile, 'w') as filew:
            filew.writelines(lines)

    def replaceLine(self, index: int, new_text: str):

        # Open a file in reading mode to read its contents
        with open(self.pathFile, 'r') as filer:
            lines = filer.readlines()

        if 0 <= index < len(lines):
            lines[index] = new_text + '\n'

            # Rewrite the entire contents of the file with the modified line
            with open(self.pathFile, 'w') as filew:
                filew.writelines(lines)
        else:
            logging.error("Invalid index, beyond file size")

    def completeLineUntil(self, length: int, lineIndex: int, char: chr):

        # Open a file in reading mode to read its contents
        with open(self.pathFile, 'r') as filer:
            lignes = filer.readlines()

        if 0 <= lineIndex < len(lignes):

            # Complete the line up to 10 characters by adding the specified character
            ligne = lignes[lineIndex].rstrip('\n')
            ligne_completee = ligne.ljust(length, char)

            # Mettre à jour la ligne dans la liste
            lignes[lineIndex] = ligne_completee + '\n'

            with open(self.pathFile, 'w') as filew:
                filew.writelines(lignes)
        else:
            logging.error("Invalid index, beyond file size")

    def addTextToLine(self, lineIndex: int, text: str):

        # Open a file in reading mode to read its contents
        with open(self.pathFile, 'r') as filer:
            lignes = filer.readlines()

        # Check if the line index is valid
        if 0 <= lineIndex < len(lignes):

            # Retrieve the line to modify
            # Add text to the end of the line
            ligne = lignes[lineIndex].rstrip('\n')
            ligne_modifiee = ligne + text + "\n"

            lignes[lineIndex] = ligne_modifiee

            with open(self.pathFile, 'w') as filew:
                filew.writelines(lignes)
        else:
            logging.error("Invalid index, beyond file size")