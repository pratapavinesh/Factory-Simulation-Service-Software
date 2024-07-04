class machinetype:
    __name=None
    __MTTF=None
    __repairTime=None
    __quantity=None

    def __init__(self, name, MTTF, repairTime, quantity):
        self.__name=name
        self.__MTTF=MTTF
        self.__repairTime=repairTime
        self.__quantity=quantity

    def getRepairTime(self):
        return self.__repairTime

    def setRepairTime(self, repairTime):
        self.__repairTime=repairTime
    
    def getQuantity(self):
        return self.__quantity
    
    def setQuantity(self, quantity):
        self.__quantity=quantity
    
    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name=name
    
    def getMTTF(self):
        return self.__MTTF
    
    def setMTTF(self, MTTF):
        self.__MTTF=MTTF

class machine:
    __ID=None
    __name=None
    __MTTF=None
    __repairTime=None
    __runningStatus=None
    __runningDays=None
    __remainingDaysToFail=None
    __remainingRepairDays=None
    __assignedAdjusterID=None

    def __init__(self, ID, name, MTTF, repairTime, runningStatus, runningDays, remainingDaysToFail, remainingRepairDays, assignedAdjusterID):
        self.__ID = ID
        self.__name = name
        self.__MTTF = MTTF
        self.__repairTime = repairTime
        self.__runningStatus = runningStatus
        self.__runningDays = runningDays
        self.__remainingDaysToFail = remainingDaysToFail
        self.__remainingRepairDays = remainingRepairDays
        self.__assignedAdjusterID = assignedAdjusterID
    
    def getID(self):
        return self.__ID

    def setID(self,ID):
        self.__ID=ID

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name=name
    
    def getMTTF(self):
        return self.__MTTF
    
    def setMTTF(self, MTTF):
        self.__MTTF=MTTF

    def getRepairTime(self):
        return self.__repairTime
    
    def setRepairTime(self, repairTime):
        self.__repairTime=repairTime
    
    def getRunningStatus(self):
        return self.__runningStatus

    def setRunningStatus(self, runningStatus):
        self.__runningStatus=runningStatus

    def getRemainingDaysToFail(self):
        return self.__remainingDaysToFail
    
    def setRemainingDaysToFail(self, remainingDaysToFail):
        self.__remainingDaysToFail=remainingDaysToFail

    def getRunningDays(self):
        return self.__runningDays
    
    def setRunningDays(self, runningDays):
        self.__runningDays=runningDays

    def getRemainingRepairDays(self):
        return self.__remainingRepairDays

    def setRemainingRepairDays(self, remainingRepairDays):
        self.__remainingRepairDays=remainingRepairDays

    def getAssignedAdjusterID(self):
        return self.__assignedAdjusterID
    
    def setAssignedAdjusterID(self, assignedAdjusterID):
        self.__assignedAdjusterID=assignedAdjusterID

class adjustertype:
    __type=None
    __expertise=[]
    __numberOfAdjusters=None

    def __init__(self, type, expertise, numberOfAdjusters):
        self.__type = type
        self.__expertise = expertise
        self.__numberOfAdjusters = numberOfAdjusters
    
    def getType(self):
        return self.__type

    def setType(self, type):
        self.__type=type
    
    def getExpertise(self):
        return self.__expertise
    
    def setExpertise(self, expertise):
        self.__expertise=expertise
    
    def getNumberOfAdjusters(self):
        return self.__numberOfAdjusters
    
    def setNumberOfAdjusters(self, numberOfAdjusters):
        self.__numberOfAdjusters=numberOfAdjusters

class adjuster:
    __ID=None
    __type=None
    __expertise=[]
    __workingStatus=None
    __workingDays=None

    def __init__(self, ID, type, expertise, workingStatus, workingDays):
        self.__ID = ID
        self.__type = type
        self.__expertise = expertise
        self.__workingStatus = workingStatus
        self.__workingDays = workingDays

    def getID(self):
        return self.__ID

    def setID(self,ID):
        self.__ID=ID

    def getType(self):
        return self.__type

    def setType(self, type):
        self.__type=type

    def getExpertise(self):
        return self.__expertise
    
    def setExpertise(self, expertise):
        self.__expertise=expertise

    def getWorkingStatus(self):
        return self.__workingStatus

    def setWorkingStatus(self, workingStatus):
        self.__workingStatus=workingStatus

    def getWorkingDays(self):
        return self.__workingDays
    
    def setWorkingDays(self, workingDays):
        self.__workingDays=workingDays