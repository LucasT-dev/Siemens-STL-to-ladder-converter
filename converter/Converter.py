import string


class Converter:

    def __init__(self, conversionType, lispRead, ladderWrite, lisp):

        self.conversionType = conversionType
        self.lispRead = lispRead
        self.ladderWrite = ladderWrite
        self.networkNumber = 0
        self.newReseau = "Network x : Title:"

        self.fileAdvandedManager = lisp

        self.lispToLadder = None

        self.RLG = None
        self.ACCU1 = None
        self.ACCU2 = None

    def start(self):

        #self.fileAdvandedManager.addLine(self.newNetwork())
        #self.fileAdvandedManager.addReturnAtLine()

        columns = 15
        rows = 300

        matrix = [["" for x in range(columns)] for y in range(rows)]


        lineEndNetwork = 0  # sauvegarde de la ligne pour la bobine du reseau

        row = 0  # ligne d'acriture des valeurs
        column = 0  # colonne d'acriture des valeurs

        newNetworks = True  # nouveau reseau a ecrire

        networkNumber = 0 # numero du réseau

        firstCondition = False

        addTiret = ""


        for i in self.lispRead:

            oldSymbol = i[:12]
            adresse = i[12:60]

            oldSymbol = oldSymbol.replace("\n", "").replace(" ", "")
            adresse = adresse.replace("\n", "").replace(" ", "")


            if oldSymbol != "":

                adresse.rstrip()
                newSymbol = self.getLadderEquivalent(oldSymbol.replace(" ", ""))
                newSymbol = newSymbol.replace("\n", "")
                addTiret = ""

                print(" -> " + oldSymbol + " -- " + adresse + " " + newSymbol)


                if (newNetworks):

                    # self.fileAdvandedManager.addLine("adress")

                    networkNumber += 1

                    row += 1

                    matrix[row][column] = "Network " + str(networkNumber) + " : Title:"

                    row += 1
                    matrix[row][column] = "Commentaire :"
                    row += 2

                    lineEndNetwork = row
                    lineEndNetwork +=1

                    newNetworks = False
                    firstCondition = True

                if oldSymbol == "U":

                    if firstCondition:
                        column += 1
                        matrix[row][column] = adresse + "  "
                        row += 1

                        # rattrapper le texte
                        if len(adresse)-7 > 0:
                            addTiret = '─' * (len(adresse)-7) + '──'

                        matrix[row][column] = "──┤ ├──" + addTiret



                        firstCondition = False

                    else:
                        column += 1
                        matrix[row-1][column] = adresse + "  "

                        # rattrapper le texte
                        if len(adresse) - 7 > 0:
                            addTiret = '─' * (len(adresse) - 7) + '──'

                        matrix[row][column] = "──┤ ├──" + addTiret

                if oldSymbol == "UN":

                    if firstCondition:
                        column += 1
                        matrix[row][column] = adresse + "  "
                        row += 1

                        # rattrapper le texte
                        if len(adresse) - 7 > 0:
                            addTiret = '─' * (len(adresse) - 7) + '──'

                        matrix[row][column] = "──┤/├──" + addTiret

                        firstCondition = False

                    else:
                        column += 1
                        matrix[row-1][column] = adresse + "  "

                        # rattrapper le texte
                        if len(adresse) - 7 > 0:
                            addTiret = '─' * (len(adresse) - 7) + '──'

                        matrix[row][column] = "──┤/├──" + addTiret

                if oldSymbol == "O":

                    if firstCondition:

                        column += 1
                        matrix[row][column] = adresse + "  "
                        row += 1

                        # rattrapper le texte
                        if len(adresse) - 7 > 0:
                            addTiret = '─' * (len(adresse) - 7) + '──'

                        matrix[row][column] = "──┤ ├──" + addTiret

                        firstCondition = False

                    else:

                        row += 2
                        matrix[row][column] = adresse + "  │"
                        row += 1

                        # rattrapper le texte
                        if len(adresse) - 7 > 0:
                            addTiret = '─' * (len(adresse) - 7) + '──┘'

                        matrix[row][column] = "──┤ ├──" + addTiret


                if oldSymbol == "ON":

                    if firstCondition:

                        column += 1
                        matrix[row][column] = adresse + "  "
                        row += 1

                        # rattrapper le texte
                        if len(adresse) - 7 > 0:
                            addTiret = '─' * (len(adresse) - 7) + '──'

                        matrix[row][column] = "──┤/├──" + addTiret

                        firstCondition = False

                    else:

                        row += 2
                        matrix[row][column] = adresse + "  │"
                        row += 1

                        # rattrapper le texte
                        if len(adresse) - 7 > 0:
                            addTiret = '─' * (len(adresse) - 7) + '──┘'

                        matrix[row][column] = "──┤/├──" + addTiret

                if oldSymbol == "=":

                    matrix[lineEndNetwork-1][9] = adresse
                    matrix[lineEndNetwork][9] = "──( )──"
                    row += 1
                    column = 0

                    #print(matrix)

                    newNetworks = True
                    


        for x in range(rows-1):

            print(matrix[x][0] + matrix[x][1] + matrix[x][2] + matrix[x][3] + matrix[x][4] + matrix[x][5] + matrix[x][6] + matrix[x][7] + matrix[x][8] + matrix[x][9])





        # if self.resultIsEndNetworks(oldSymbol):

        # self.ladderWrite.write(result)

        # self.lineReturn(2)
        # self.ladderWrite.write(self.newNetwork() + "\n")

        # else:

        # self.ladderWrite.write(str(result))

    def newNetwork(self) -> string:

        self.networkNumber += 1
        string = self.newReseau

        return string.replace("x", str(self.networkNumber))

    def getLadderEquivalent(self, lispLetter) -> string:

        self.openLispToLadderFile()

        for i in self.lispToLadder:

            s = i.split(":")[0]
            s1 = i.split(":")[1]

            s = s.replace(" ", "")
            lispLetter = lispLetter.replace(" ", "")

            # print("S TEST :" + s)
            # print("LISP TEST :" + lispLetter)

            if s == lispLetter:
                # s.replace("\n", "")

                # print("Equivalent :" + s1)

                self.closeLispToLadderFile()
                return s1

        return "NOPE"

    def lineReturn(self, number: int):

        for i in range(number):
            self.ladderWrite.write("\n")

    def openLispToLadderFile(self):
        self.lispToLadder = open("resources/LispToLadder.txt", "r")

    def closeLispToLadderFile(self):
        self.lispToLadder.close()

    def resultIsEndNetworks(self, result: string) -> bool:

        result.replace(" ", "")

        if result == "=" or result == "R" or result == "S":
            return True

        else:
            return False
