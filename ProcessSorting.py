from DataGenerator import listOfProcesses, save, returnNumberOfProcesses


class FCFS:
    def __init__(self):
        self.processesList = []
        self.readyProcess = []
        self.numberOfProcesses = returnNumberOfProcesses()
        self.processesList = listOfProcesses(self.numberOfProcesses)
        save()
        self.processesList.loadListOfProcess("allProcesses.txt")
        self.time = 0
        self.addedToList = 0
        self.sortedTuples = []


    def algorithm(self):

        for i in range(0, self.numberOfProcesses):
            if self.processesList.process[i].incomeTime == str(self.time):
                self.readyProcess.append(self.processesList.process[i])
                self.addedToList = self.addedToList + 1

        self.time = self.time + 1


    def SJF(self):
        self.algorithm()

    def sortSJF(self):
        length = len(self.readyProcess)
        if length >= 2:
            for i in range(length - 1):
                for j in range(0, length - i - 1):
                    if int(self.readyProcess[j].processingTime) > int(self.readyProcess[j + 1].processingTime):
                        self.readyProcess[j], self.readyProcess[j + 1] = self.readyProcess[j + 1], self.readyProcess[j]
