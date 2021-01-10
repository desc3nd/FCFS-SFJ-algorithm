import random


class oneProcessGenerate:
    def __init__(self, name):
        self.name = name
        self.processStatus = "New"
        self.arrivalTime = 0
        self.processingTime = 0
        self.finishTime = 0
        self.waitingTime = 0

    def generateRandom(self):
        self.arrivalTime = random.randint(1, 4)
        self.processingTime = random.randint(1, 4)


class listOfProcesses:
    def __init__(self, numberOfProcesses):
        self.numberOfProcesses = numberOfProcesses
        self.myprocess = oneProcessGenerate
        self.process = []
        self.listOfLines = []
        for counter in range(0, numberOfProcesses):
            self.process.append(self.myprocess(str(counter)))
            self.process[counter].generateRandom()

    def viewProcesses(self):
        for i in range(0, self.numberOfProcesses):
            print("name:", self.process[i].name, "arrivalTime:", self.process[i].arrivalTime, "processingTime: ",
                  self.process[i].processingTime, "FinishTime: ", self.process[i].finishTime, "WaitingTime: ",
                  self.process[i].waitingTime)

    def saveListOfProcesses(self, fileName):
        try:
            file = open(fileName, 'w')
        except Exception as exc:
            print("Nie mozna otworzyc pliku:", exc)
        for i in range(0, self.numberOfProcesses):
            file.write("name of process: ")
            file.write('\n')
            file.write(str(self.process[i].name))
            file.write('\n')
            file.write("arrival Time: ")
            file.write('\n')
            file.write(str(self.process[i].arrivalTime))
            file.write('\n')
            file.write("processing Time: ")
            file.write('\n')
            file.write(str(self.process[i].processingTime))
            file.write('\n')
            file.write("finish Time: ")
            file.write('\n')
            file.write(str(self.process[i].finishTime))
            file.write('\n')
            file.write("waiting Time: ")
            file.write('\n')
            file.write(str(self.process[i].waitingTime))
            file.write('\n')
        try:
            file.close()
        except Exception as exc:
            print("Nie mozna zamknac pliku:", exc)

    def loadListOfProcess(self, fileName):
        try:
            with open(fileName) as self.file:
                self.listOfLines = self.file.read().splitlines()
        except Exception as exc:
            print("Nie mozna otworzyc pliku:", exc)
        jumper = 1
        for i in range(0, self.numberOfProcesses):
            self.process[i].name = self.listOfLines[jumper]
            jumper = jumper + 2
            self.process[i].arrivalTime = self.listOfLines[jumper]
            jumper = jumper + 2
            self.process[i].processingTime = self.listOfLines[jumper]
            jumper = jumper + 2
            self.process[i].finishTime = self.listOfLines[jumper]
            jumper = jumper + 2
            self.process[i].waitingTime = self.listOfLines[jumper]
            jumper = jumper + 2
        try:
            self.file.close()
        except Exception as exc:
            print("Nie mozna zamknac pliku:", exc)


def returnNumberOfProcesses():
    numberOfProcesses = 3
    return numberOfProcesses


procesiki = listOfProcesses(returnNumberOfProcesses())


def save():
    procesiki.saveListOfProcesses("allProcesses.txt")
