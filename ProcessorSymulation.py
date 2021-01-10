from DataGenerator import listOfProcesses, save, returnNumberOfProcesses
from ProcessSorting import Algorithm
from math import sqrt


class simulation:
    def __init__(self, algorithm):
        self.numberOfProcesses = returnNumberOfProcesses()
        self.algorithm = algorithm
        save()
        self.processesList = listOfProcesses(self.numberOfProcesses)
        self.processesList.loadListOfProcess("allProcesses.txt")
        self.Algorithm = Algorithm()
        self.processingTime = 100
        self.inProgress = False
        self.procCount = 0
        self.averageArrivalTime = 0
        self.averageProcessingTime = 0
        self.averageFinishTime = 0
        self.averageWaitingTime = 0
        self.standardDeviationArrivalTime = 0
        self.standardDeviationProcessingTime = 0
        self.standardDeviationFinishTime = 0
        self.standardDeviationWaitingTime = 0

    def checkReadyProcesses(self):
        if len(
                self.Algorithm.readyProcess) != 0 and self.inProgress == False:  # wlacz proces do dzialania!
            self.inProgress = True
            self.processingTime = int(self.Algorithm.readyProcess[0].processingTime)
            self.processesList.process[self.procCount] = self.Algorithm.readyProcess[0]
            self.processesList.process[self.procCount].waitingTime = self.Algorithm.time - int(
                self.processesList.process[self.procCount].arrivalTime) - 1

    def checkIfProcessInProgress(self):
        if self.inProgress:
            self.processingTime = self.processingTime - 1

    def startSymFCFS(self):
        while self.numberOfProcesses > 0:
            if self.algorithm == "FCFS":
                self.Algorithm.CreateReadyProcessList()
                self.checkReadyProcesses()
                self.checkIfProcessInProgress()
                if self.processingTime <= 0 and self.inProgress:
                    self.inProgress = False
                    self.numberOfProcesses = self.numberOfProcesses - 1
                    self.processesList.process[self.procCount].finishTime = self.Algorithm.time
                    self.procCount = self.procCount + 1
                    if self.numberOfProcesses == 0:
                        self.numberOfProcesses = returnNumberOfProcesses()
                        break
                    del self.Algorithm.readyProcess[0]

    def startSymSJF(self):
        while self.numberOfProcesses > 0:
            self.Algorithm.CreateReadyProcessList()
            if self.inProgress == False:
                self.Algorithm.sortSJF()
            if len(
                    self.Algorithm.readyProcess) != 0 and self.inProgress == False:  # wlacz proces do dzialania!
                self.inProgress = True
                self.processingTime = int(self.Algorithm.readyProcess[0].processingTime)
                self.processesList.process[self.procCount] = self.Algorithm.readyProcess[0]
                self.processesList.process[self.procCount].waitingTime = self.Algorithm.time - int(
                    self.processesList.process[self.procCount].arrivalTime) - 1
            if self.inProgress:
                self.processingTime = self.processingTime - 1
            if self.processingTime <= 0 and self.inProgress:
                self.inProgress = False
                self.numberOfProcesses = self.numberOfProcesses - 1
                self.processesList.process[self.procCount].finishTime = self.Algorithm.time
                self.procCount = self.procCount + 1
                if self.numberOfProcesses == 0:
                    self.numberOfProcesses = returnNumberOfProcesses()
                    break
                del self.Algorithm.readyProcess[0]

    def statistic(self):
        for i in range(0, self.numberOfProcesses):
            self.averageArrivalTime = self.averageArrivalTime + int(
                self.processesList.process[i].arrivalTime) / self.numberOfProcesses
            self.averageProcessingTime = self.averageProcessingTime + int(
                self.processesList.process[i].processingTime) / self.numberOfProcesses
            self.averageFinishTime = self.averageFinishTime + int(
                self.processesList.process[i].finishTime) / self.numberOfProcesses
            self.averageWaitingTime = self.averageWaitingTime + int(
                self.processesList.process[i].waitingTime) / self.numberOfProcesses
        for i in range(0, self.numberOfProcesses):
            self.standardDeviationArrivalTime = self.standardDeviationArrivalTime + sqrt((int(
                self.processesList.process[i].arrivalTime) - self.averageArrivalTime) ** 2) / self.numberOfProcesses
            self.standardDeviationProcessingTime = self.standardDeviationProcessingTime + sqrt((int(
                self.processesList.process[
                    i].processingTime) - self.averageProcessingTime) ** 2) / self.numberOfProcesses
            self.standardDeviationFinishTime = self.standardDeviationFinishTime + sqrt(
                (int(self.processesList.process[i].finishTime) - self.averageFinishTime) ** 2) / self.numberOfProcesses
            self.standardDeviationWaitingTime = self.standardDeviationWaitingTime + sqrt((int(
                self.processesList.process[i].waitingTime) - self.averageWaitingTime) ** 2) / self.numberOfProcesses

    def printStatistic(self):
        print("average Arrival Time:", round(self.averageArrivalTime,3), "+-", round(self.standardDeviationArrivalTime,3))
        print("average Processing Time:", round(self.averageProcessingTime,3), "+-", round(self.standardDeviationProcessingTime,3))
        print("average Finish Time:", round(self.averageFinishTime,3), "+-", round(self.standardDeviationFinishTime,3))
        print("average Waiting Time:", round(self.averageWaitingTime,3), "+-", round(self.standardDeviationWaitingTime,3))
    def printOutcome(self):
        self.processesList.viewProcesses()
        self.printStatistic()

    def safeStatistic(self, stat, stat2, name):

        self.file.write(str(name))
        self.file.write(str(round(stat, 3)))
        self.file.write(" +- ")
        self.file.write(str(round(stat2, 3)))
        self.file.write("\n")

    def saveInFile(self, fileName):
        self.statistic()
        try:
            self.file = open(fileName, 'w')
        except Exception as exc:
            print("Nie mozna otworzyc pliku:", exc)
        for i in range(0, len(self.processesList.process)):
            self.file.write("name of process: \n")
            self.file.write(str(self.processesList.process[i].name))
            self.file.write('\n')
            self.file.write("arrival Time: \n")
            self.file.write(str(self.processesList.process[i].arrivalTime))
            self.file.write('\n')
            self.file.write("Processing Time: \n")
            self.file.write(str(self.processesList.process[i].processingTime))
            self.file.write('\n')
            self.file.write("Finish Time: \n")
            self.file.write(str(self.processesList.process[i].finishTime))
            self.file.write('\n')
            self.file.write("waiting Time: \n")
            self.file.write(str(self.processesList.process[i].waitingTime))
            self.file.write('\n-------------------------------\n')
        self.safeStatistic(self.averageArrivalTime, self.standardDeviationArrivalTime, "average arrival time: ")
        self.safeStatistic(self.averageProcessingTime, self.standardDeviationProcessingTime,
                           "average processing time: ")
        self.safeStatistic(self.averageFinishTime, self.standardDeviationFinishTime, "average finish time: ")
        self.safeStatistic(self.averageWaitingTime, self.standardDeviationWaitingTime, "average waiting time: ")
        try:
            self.file.close()
        except Exception as exc:
            print("Nie mozna zamknac pliku:", exc)






FCFS = simulation("FCFS")
SJF = simulation("FCFS")
FCFS.startSymFCFS()
SJF.startSymSJF()

FCFS.printOutcome()
FCFS.saveInFile("FCFSoutcome.txt")

SJF.saveInFile("SJFoutcome.txt")
print("sjf")
SJF.printOutcome()
