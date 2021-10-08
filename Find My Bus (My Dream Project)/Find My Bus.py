from busSchedule import timeTable, busList, stageList


# ----------------- Getting Bus Details -----------------#
def busDetail(busName):
    if busName in busList:
        print("-" * 45)
        print("Time Schedule of", busName + ':')
        for x, y in timeTable[busName].items():
            print(x, ':', y)
        print("-" * 45)


# ----------------- usingBus -----------------#
def usingBus():
    print("Available Bus List:", sorted(busList))
    while True:
        busName = input("\nEnter Bus Name: ")
        if busName in busList:
            busDetail(busName)
            break
        else:
            print("Sorry we have no data about", busName)


# ----------------- using Stage -----------------#
def usingStage():
    print("\nAvailable Stages:", sorted(stageList))
    stageName = input("\nEnter Stage Name: ")
    result = set()
    if stageName in stageList:
        for bus in timeTable:
            for stage in timeTable[bus].values():
                if stage == stageName:
                    result.add(bus)
        while True:
            print("\nAvailable Buses for", stageName + ':')
            no = 1
            for bus in sorted(result):
                print(str(no) + '.', bus)
                no += 1
            busName = input("\nEnter the bus name to show its schedule: ")
            if busName in result:
                busDetail(busName)
                break
            else:
                print("Incorrect input! Please Try again.")
    else:
        print("Invalid Selection! Please try again.")
        usingStage()


# ----------------- using Stages -----------------#
def usingStages():
    print("\nAvailabe stages:", sorted(stageList))
    while True:
        stage1 = input("\nEnter your Origin: ")
        if stage1 not in stageList:
            print("Entered Origin is not available in our data! Please try with another.")
        else:
            break
    while True:
        stage2 = input("\nEnter your Destination: ")
        if stage2 not in stageList:
            print("Entered Destination is not available in our data! Please try with another.")
        else:
            break
    no = 1
    available_bus = []
    for bus in timeTable:
        if stage1 in timeTable[bus].values():
            if stage2 in timeTable[bus].values():
                available_bus.append(bus)
                print("\nAvailable Buses for", stage1, '-', stage2)
                print(str(no) + ".", bus)
                no += 1
    if len(available_bus) != 0:
        while True:
            busName = input("\nEnter the bus name to know its schedule: ")
            if busName in available_bus:
                busDetail(busName)
                break
            else:
                print(busName, "is not available for", stage1, "-", stage2 + ".", "Try again!")
    else:
        print("No direct bus available for", stage1, "-", stage2)


# ----------------- Welcome Screen -----------------#
def appFunctions():
    while True:
        print("""\nWhat is your need?
    1. Bus detail
    2. Bus details for a specific stage
    3. Bus details between two stages""")
        choise = input("\nEnter your choise: ")
        if choise == "1":
            usingBus()
        elif choise == "2":
            usingStage()
        elif choise == '3':
            usingStages()
        else:
            print("\nProgram aborted by wrong input!")
            break


appFunctions()
