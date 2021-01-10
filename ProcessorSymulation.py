from DataGenerator import listOfProcesses, save, returnNumberOfProcesses
from ProcessSorting import FCFS


class simulation:
    def __init__(self, algorithm):
        self.numberOfProcesses = returnNumberOfProcesses()
        self.algorithm = algorithm
        save()
        self.processesList = listOfProcesses(self.numberOfProcesses)
        self.processesList.loadListOfProcess("allProcesses.txt")
        if self.algorithm == "FCFS":
            self.firstComeFirstServed = FCFS()
        self.processingTime = 100
        self.inProgress = False
        self.procCount = 0

    def testy(self):
        self.processesList.viewProcesses()
        print(self.firstComeFirstServed.readyProcess)

    def checkReadyProcesses(self):
        if len(
                self.firstComeFirstServed.readyProcess) != 0 and self.inProgress == False:  # wlacz proces do dzialania!
            self.inProgress = True
            self.processingTime = int(self.firstComeFirstServed.readyProcess[0].processingTime)
            self.processesList.process[self.procCount] = self.firstComeFirstServed.readyProcess[0]
            self.processesList.process[self.procCount].waitingTime = self.firstComeFirstServed.time - int(
                self.processesList.process[self.procCount].incomeTime) - 1



    def checkIfProcessInProgress(self):
        if self.inProgress:
            self.processingTime = self.processingTime - 1

    def startSym(self):
        while self.numberOfProcesses > 0:
            if self.algorithm == "FCFS":
                self.firstComeFirstServed.algorithm()
                self.checkReadyProcesses()
                self.checkIfProcessInProgress()
                if self.processingTime <= 0 and self.inProgress:
                    self.inProgress = False
                    self.numberOfProcesses = self.numberOfProcesses - 1
                    self.processesList.process[self.procCount].finishTime = self.firstComeFirstServed.time
                    self.procCount = self.procCount + 1
                    if self.numberOfProcesses == 0:
                        self.numberOfProcesses = returnNumberOfProcesses()
                        break
                    del self.firstComeFirstServed.readyProcess[0]

    def startAnotherSym(self):
        while self.numberOfProcesses > 0:
            self.firstComeFirstServed.algorithm()
            if self.inProgress==False:
                self.firstComeFirstServed.sortSJF()
            if len(
                    self.firstComeFirstServed.readyProcess) != 0 and self.inProgress == False:  # wlacz proces do dzialania!
                self.inProgress = True
                self.processingTime = int(self.firstComeFirstServed.readyProcess[0].processingTime)
                self.processesList.process[self.procCount] = self.firstComeFirstServed.readyProcess[0]
                self.processesList.process[self.procCount].waitingTime = self.firstComeFirstServed.time - int(
                    self.processesList.process[self.procCount].incomeTime) - 1
            if self.inProgress:
                self.processingTime = self.processingTime - 1
            if self.processingTime <= 0 and self.inProgress:
                self.inProgress = False
                self.numberOfProcesses = self.numberOfProcesses - 1
                self.processesList.process[self.procCount].finishTime = self.firstComeFirstServed.time
                self.procCount = self.procCount + 1
                if self.numberOfProcesses == 0:
                    self.numberOfProcesses = returnNumberOfProcesses()
                    break
                del self.firstComeFirstServed.readyProcess[0]

    def printOutcome(self):
        self.processesList.viewProcesses()

    def saveInFile(self, fileName):
        try:
            file = open(fileName, 'w')
        except Exception as exc:
            print("Nie mozna otworzyc pliku:", exc)
        for i in range(0, len(self.processesList.process)):
            file.write("name of process: \n")
            file.write(str(self.processesList.process[i].name))
            file.write('\n')
            file.write("income Time: \n")
            file.write(str(self.processesList.process[i].incomeTime))
            file.write('\n')
            file.write("Processing Time: \n")
            file.write(str(self.processesList.process[i].processingTime))
            file.write('\n')
            file.write("Finish Time: \n")
            file.write(str(self.processesList.process[i].finishTime))
            file.write('\n')
            file.write("waiting Time: \n")
            file.write(str(self.processesList.process[i].waitingTime))
            file.write('\n-------------------------------\n')
        try:
            file.close()
        except Exception as exc:
            print("Nie mozna zamknac pliku:", exc)


simulationen = simulation("FCFS")
simulationen2 = simulation("FCFS")
simulationen.testy()
simulationen2.startAnotherSym()
simulationen.startSym()
simulationen.printOutcome()
simulationen.saveInFile("FCFSoutcome.txt")

simulationen2.saveInFile("SJFoutcome.txt")
print("sjf")
simulationen2.printOutcome()

# class simulation(DataGenerator.oneProcessGenerate):
#     def __init__(self, algorithm):
#         self.process = []
#         self.algorithm = algorithm
#         self.numberOfProcess = DataGenerator.returnNumberOfProcess()
#       #  for i in range(0, self.numberOfProcess):
#            # self.process.append(DataGenerator.oneProcessGenerate(str(i)))
#
#         self.readyProcess = []
#         self.finishedProcess = []
#         self.processingTime = 10000
#         self.processInSymulating=False
#         if self.algorithm == "FCFS":
#             self.choosenAlgorithm = ProcessSorting.FCFS()
#             self.time = self.choosenAlgorithm.iter
#     def symRunning(self):
#         while self.numberOfProcess > 0:
#             self.choosenAlgorithm.checkIncomeTime()
#             if len(self.choosenAlgorithm.readyProcess) != 0 and self.processInSymulating == False:
#                 self.processInSymulating=True
#                 self.processingTime = self.choosenAlgorithm.readyProcess[0].processingTime
#                 print("in if name",self.choosenAlgorithm.readyProcess[0].name)
#                 print("in if processingTime", self.choosenAlgorithm.readyProcess[0].processingTime)
#                 print("in if income", self.choosenAlgorithm.readyProcess[0].incomeTime)
#             if self.processingTime <= 0 and self.processInSymulating == True:
#                 print("czywchodzi")
#                 self.processInSymulating = False
#                 self.finishedProcess.append(self.choosenAlgorithm.readyProcess[0])
#                 #self.process[int(self.choosenAlgorithm.readyProcess[0].name)].processStatus = "FINISHED"
#                 #self.process[int(self.choosenAlgorithm.readyProcess[0].name)].finishTime = self.choosenAlgorithm.iter
#                 del self.choosenAlgorithm.readyProcess[0]
#              #   del self.process[int(self.choosenAlgorithm.readyProcess[0].name)]
#                 self.numberOfProcess = self.choosenAlgorithm.numberOfProcess - 1
#             print("processing time:",self.processingTime)
#             self.processingTime = self.processingTime - 1
#         #print(self.process[int(self.readyProcess[0].name)].finishTime)
#
#     # print("DUPA")
#
#
# sym = simulation("FCFS")
# sym.symRunning()
