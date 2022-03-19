import re


class HashTable():
    def __init__(self):
        self.array = [[] for i in range(10)]

    def computeHash(self, key):
        h = 0
        for ch in key:
            h += ord(ch)
        return h % 10

    def hashKey(self, key):
        k = self.computeHash(key)
        for i, val in enumerate(self.array[k]):
            if val[0] == key:
                return True
            return False

    def addRecord(self, key, value):
        k = self.computeHash(key)
        found = False
        for index, ele in enumerate(self.array[k]):
            if ele[0] == key:
                self.array[ele][index] = (key, value)
                found = True
                break
        if found == False:
            self.array[k].append((key, value))

    def getRecord(self, key):
        k = self.computeHash(key)
        for val in self.array[k]:
            if val[0] == key:
                return val[1]

    def deleteRecord(self, key):
        k = self.computeHash(key)
        for i, val in enumerate(self.array[k]):
            if val[0] == key:
                self.array[k].remove(self.array[val][i])


def CreateOpTable():
    OpTable = HashTable()
    OpTable.addRecord("MOV", [44, 2, 4])
    OpTable.addRecord("ADD", [47, 2, 4])
    OpTable.addRecord("JUMP", [67, 1, 2])
    OpTable.addRecord("CMP", [23, 2, 4])
    OpTable.addRecord("START", [])
    OpTable.addRecord("END", [])
    return OpTable


def CreateRegisterTable():
    RegTable = HashTable()
    RegTable.addRecord("A", ["000"])
    RegTable.addRecord("B", ["001"])
    RegTable.addRecord("C", ["010"])
    RegTable.addRecord("D", ["100"])
    return RegTable


def CreateSymbolTable():
    symbolTable = HashTable()
    return symbolTable


class Assembler():
    def __init__(self):
        self.Optable = CreateOpTable()
        self.RegisteTable = CreateRegisterTable()
        self.symbolTable = CreateSymbolTable()
        self.pointer = 0

    def loadFile(self, file):
        f = open(file, mode='r')
        l = f.read()
        return l.split("\n")

    def printSymbolTable(self):
        for i in self.symbolTable.array:
            if i:
                for j in i:
                    if int(j[1]) == -1:
                        print(j[0] + "  was never defined in the program")
                    else:
                        print(j[0] + "," + " " + str(j[1]))

    def checkHex(self, s):
        for i in range(len(s)):
            ch = s[i]
            if ch < '0' or ch > '9':
                return False
        return True

    def validateLine(self, line, i, s):
        error = False
        # validate start line
        e = False
        if i == 0 and line[0] == 'START' and len(line) == 2:
            e = True
            self.pointer = int(line[1])
        if e == False and i == 0:
            print(f"Line {i + 1} invalid start")
            error = True
        # validate last line
        f = False
        if i == len(s) - 1 and line[0] == "END":
            f = True
        if f == False and i == len(s) - 1:
            print(f"Line {i + 1} invalid end")
            error = True
        # validate BYTE line

        if line[0] == "BYTE":
            if len(line[1:]) == 2:
                if line[1][0].isalpha() and line[1][1:].isalnum() and line[2][0] == '#' and line[2][1:].isnumeric():
                    self.symbolTable.addRecord(line[1], self.pointer)
                    self.pointer += 1
                    pass
                else:
                    error = True
                    print(f"Line {i + 1}: Invalid operand")
            else:
                error = True
                print(f"Line {i + 1} : Invalid # of operands for BYTE")
        # validate MOV Statement
        elif line[0] == "MOV":
            record = self.Optable.getRecord(line[0])
            # print(record)
            if len(line[1:]) == int(record[1]):
                if (self.RegisteTable.hashKey(line[1]) or self.symbolTable.hashKey(line[1])) and (
                        self.RegisteTable.hashKey(line[2]) or (line[2][0] == "#" and line[2][1:].isnumeric())):
                    self.pointer += int(record[2])
                    pass
                else:
                    error = True
                    print(f"Line {i + 1} : Invalid Operand")
            else:
                error = True
                print(f"Line {i + 1} Invalid of # operands")
        # validate ADD statement
        elif line[0] == "ADD":
            record = self.Optable.getRecord(line[0])
            # print(record)
            if len(line[1:]) == int(record[1]):
                if (self.RegisteTable.hashKey(line[1]) or self.symbolTable.hashKey(line[1])) and (
                        (line[2][0] == "#" and line[2][1:].isnumeric()) or self.RegisteTable.hashKey(
                        line[2] or self.symbolTable.hashKey(line[2]))):
                    self.pointer += int(record[2])
                    pass
                else:
                    error = True
                    print(f"Line {i + 1} : Invalid operand for ADD")
            else:
                error = True
                print(f"Line {i + 1} Invalid # of operands for ADD")
        # validate JUMP statement
        elif line[0] == "JUMP":
            record = self.Optable.getRecord(line[0])
            if len(line[1:]) == int(record[1]):
                if line[1][0].isalpha() and self.symbolTable.hashKey(line[1]):
                    pass
                else:
                    error = True
                    #print(f"Line {i + 1}: {line[1]} was never declared in the program")
                    self.pointer += record[2]
                    self.symbolTable.addRecord(line[1], -1)
            else:
                error = True
                print(f"Line {i + 1}: Invalid # of operands")
        # validate LX: statement
        elif line[0][-1] == ":":
            # print(line[0],line[1])
            lbl = line[0].split(":")[0]
            # print(lbl)
            if lbl[0].isalpha() and lbl[1:].isalnum():
                temp = self.pointer
                isStatement = self.validateLine(line[1:], i, s)
                if isStatement:
                    print(f" {line[0]}:Invalid Label")
                else:
                    self.symbolTable.addRecord(lbl, temp)
        # unknown operation
        else:
            if line[0] == "START" or line[0] == "END":
                pass
            else:
                #print(f"Line{i + 1}: unkown operation {line[0]}")
                error = True

        return error

    def validateCode(self, file):
        s = self.loadFile(file)
        # print(s)
        for i in range(len(s)):
            li = []
            list = re.split(",| ", s[i])
            for j in range(len(list)):  # remove all spaces
                if list[j] != '':
                    li.append(list[j])
            # print(li)
            temp = self.validateLine(li, i, s)
            if temp:
                error = True
        return error


if __name__ == '__main__':
    check = Assembler()

    print(
        "------------------------------------------------------------------------------------------------------------")
    file = str(input("Enter file name:"))
    isvalidate = check.validateCode(file)
    check.printSymbolTable()
    if isvalidate:
        print("ASSEMBLER: Found some errors in your program. Cannot proceed!\n")
    else:
        print("Succesfull\n")
    print(
        "------------------------------------------------------------------------------------------------------------")