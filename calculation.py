from classes import machinetype, machine, adjustertype, adjuster


def simulate(adjustersList, machinesList, numberOfYears):
    machinetypes=[]
    adjustertypes=[]
    for unitMachine in machinesList:
        machinetypes.append(machinetype(unitMachine["machineName"],unitMachine["MTTF"],unitMachine["repairTime"],unitMachine["quantity"]))
    for unitAdjuster in adjustersList:
        adjustertypes.append(adjustertype(unitAdjuster["adjusterType"],unitAdjuster["expertise"],unitAdjuster["numberOfAdjusters"]))
    machines=[]
    adjusters=[]
    
    machineidx=1
    for var in machinetypes:
        quantity=var.getQuantity()
        for i in range(quantity):
            machines.append(machine(machineidx,var.getName(),var.getMTTF(),var.getRepairTime(),1,0,var.getMTTF(),0,0))
            machineidx+=1

    adjusteridx=1
    for var in adjustertypes:
        numberOfAdjusters=var.getNumberOfAdjusters()
        for i in range(numberOfAdjusters):
            adjusters.append(adjuster(adjusteridx,var.getType(),var.getExpertise(),0,0))
            adjusteridx+=1


    days=numberOfYears*365
    for day in range(0,days):
        for unitMachine in machines:
            if unitMachine.getRunningStatus()==0 and unitMachine.getRemainingRepairDays()==0:
                assignedAdjusterID=unitMachine.getAssignedAdjusterID()
                for unitAdjuster in adjusters:
                    if unitAdjuster.getID()==assignedAdjusterID:
                        unitAdjuster.setWorkingStatus(0)
                        break
                unitMachine.setRunningStatus(1)
                unitMachine.setRemainingDaysToFail(unitMachine.getMTTF())
                unitMachine.setAssignedAdjusterID(0)
        
        for unitMachine in machines:
            if unitMachine.getRemainingDaysToFail()==0:
                unitMachine.setRunningStatus(0)
        
        for unitMachine in machines:
            if unitMachine.getRunningStatus()==1:
                unitMachine.setRunningDays(unitMachine.getRunningDays()+1)
                unitMachine.setRemainingDaysToFail(unitMachine.getRemainingDaysToFail()-1)
            else:
                if unitMachine.getAssignedAdjusterID()!=0:
                    unitMachine.setRemainingRepairDays(unitMachine.getRemainingRepairDays()-1)
                    assignedAdjusterID=unitMachine.getAssignedAdjusterID()
                    for unitAdjuster in adjusters:
                        if unitAdjuster.getID()==assignedAdjusterID:
                            unitAdjuster.setWorkingDays(unitAdjuster.getWorkingDays()+1)
                            break
                else:
                    for unitAdjuster in adjusters:
                        if unitAdjuster.getWorkingStatus()==0 and (unitMachine.getName() in unitAdjuster.getExpertise()):
                            unitAdjuster.setWorkingStatus(1)
                            unitMachine.setAssignedAdjusterID(unitAdjuster.getID())
                            unitMachine.setRemainingRepairDays(unitMachine.getRepairTime())

                            unitMachine.setRemainingRepairDays(unitMachine.getRemainingRepairDays()-1)
                            unitAdjuster.setWorkingDays(unitAdjuster.getWorkingDays()+1)
                            break


    totalMachineRunningDays=0
    totalAdjusterWorkingDays=0
    for unitMachine in machines:
        totalMachineRunningDays+=unitMachine.getRunningDays()

    for unitAdjuster in adjusters:
        totalAdjusterWorkingDays+=unitAdjuster.getWorkingDays()

    machineUtilization=totalMachineRunningDays/(days*len(machines))
    adjusterUtilization=totalAdjusterWorkingDays/(days*len(adjusters))

    utilization={}
    utilization["avg_machine_util"]=round(machineUtilization*100,2)
    utilization["avg_adjuster_util"]=round(adjusterUtilization*100,2)

    utilization["machine_util"]={}
    utilization["adjuster_util"]={}

    
    for unitMachine in machinesList:
        runningDays=0
        count=0
        machineName=unitMachine["machineName"]
        for iterator in machines:
            if iterator.getName()==machineName:
                runningDays+=iterator.getRunningDays()
                count+=1
        utilization["machine_util"][machineName]=round(100*(runningDays/(days*count)),2)

    for unitAdjuster in adjustersList:
        workingDays=0
        count=0
        adjusterType=unitAdjuster["adjusterType"]
        for iterator in adjusters:
            if iterator.getType()==adjusterType:
                workingDays+=iterator.getWorkingDays()
                count+=1
        utilization["adjuster_util"][adjusterType]=round(100*(workingDays/(days*count)),2)
    
    return utilization


# machinetypes=[
#                 machinetype("Lathe",10,2,10),
#                 machinetype("Drill",15,1,20),
#                 machinetype("Mill",30,4,8)
#             ]

# adjustertypes=[
#                 adjustertype(1,["Lathe","Drill"],10),
#                 adjustertype(2,["Mill"],100)
#             ]

# machines=[]
# adjusters=[]

# machineidx=1
# for var in machinetypes:
#     quantity=var.getQuantity()
#     for i in range(quantity):
#         machines.append(machine(machineidx,var.getName(),var.getMTTF(),var.getRepairTime(),1,0,var.getMTTF(),0,0))
#         machineidx+=1

# adjusteridx=1
# for var in adjustertypes:
#     numberOfAdjusters=var.getNumberOfAdjusters()
#     for i in range(numberOfAdjusters):
#         adjusters.append(adjuster(adjusteridx,var.getType(),var.getExpertise(),0,0))
#         adjusteridx+=1


# numberOfYears=2
# days=numberOfYears*365


# for day in range(0,days):
#     for machine in machines:
#         if machine.getRunningStatus()==0 and machine.getRemainingRepairDays()==0:
#             assignedAdjusterID=machine.getAssignedAdjusterID()
#             for adjuster in adjusters:
#                 if adjuster.getID()==assignedAdjusterID:
#                     adjuster.setWorkingStatus(0)
#                     break
#             machine.setRunningStatus(1)
#             machine.setRemainingDaysToFail(machine.getMTTF())
#             machine.setAssignedAdjusterID(0)
    
#     for machine in machines:
#         if machine.getRemainingDaysToFail()==0:
#             machine.setRunningStatus(0)
    
#     for machine in machines:
#         if machine.getRunningStatus()==1:
#             machine.setRunningDays(machine.getRunningDays()+1)
#             machine.setRemainingDaysToFail(machine.getRemainingDaysToFail()-1)
#         else:
#             if machine.getAssignedAdjusterID()!=0:
#                 machine.setRemainingRepairDays(machine.getRemainingRepairDays()-1)
#                 assignedAdjusterID=machine.getAssignedAdjusterID()
#                 for adjuster in adjusters:
#                     if adjuster.getID()==assignedAdjusterID:
#                         adjuster.setWorkingDays(adjuster.getWorkingDays()+1)
#                         break
#             else:
#                 for adjuster in adjusters:
#                     if adjuster.getWorkingStatus()==0 and (machine.getName() in adjuster.getExpertise()):
#                         adjuster.setWorkingStatus(1)
#                         machine.setAssignedAdjusterID(adjuster.getID())
#                         machine.setRemainingRepairDays(machine.getRepairTime())

#                         machine.setRemainingRepairDays(machine.getRemainingRepairDays()-1)
#                         adjuster.setWorkingDays(adjuster.getWorkingDays()+1)
#                         break


# totalMachineRunningDays=0
# totalAdjusterWorkingDays=0
# for machine in machines:
#     totalMachineRunningDays+=machine.getRunningDays()

# for adjuster in adjusters:
#     totalAdjusterWorkingDays+=adjuster.getWorkingDays()

# machineUtilization=totalMachineRunningDays/(days*len(machines))
# adjusterUtilization=totalAdjusterWorkingDays/(days*len(adjusters))

# print(f"Machine Utilization: {round(machineUtilization*100,2)}%")
# print(f"Adjuster Utilization: {round(adjusterUtilization*100,2)}%")
