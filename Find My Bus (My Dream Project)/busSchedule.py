# ----------------- Bus Time Table -----------------#
timeTable = {
    "Sharanya": {
        "08:35": "Chennai",
        "09:00": "Salem",
        "09:25": "Erode",
        "09:50": "Tiruppur",
        "10:20": "Coimbatore",
    },
    "DNC": {
        "08:35": "Kanniyakumari",
        "09:00": "Tutikorin",
        "09:25": "Namakkal",
        "09:50": "Trichy",
        "10:20": "Madurai",
    },
    "Balamurugan": {
        "08:35": "Thiruvallur",
        "09:00": "Dharmapuri",
        "09:25": "Krishnagiri",
        "09:50": "Hosur",
        "10:20": "Kadathur",
    },
    "Selvi": {
        "08:35": "Dharmapuri",
        "09:00": "Kadathur",
        "09:25": "Bommidi",
        "09:50": "Pappireddipatti",
        "10:20": "Pallipatti",
    },
    "Senthil": {
        "08:35": "Menasi",
        "09:00": "Molayanur",
        "09:25": "Thurinjipatti",
        "09:50": "Nadur",
        "10:20": "London",
    },
}

# ----------------- Preparing Stages and Buses -----------------#
stages = set()
for x in timeTable.keys():
    for z in timeTable[x].values():
        stages.add(z)

# ----------------- Prepared Stages and Buses -----------------#
busList = list(sorted(timeTable.keys()))
stageList = list(sorted(stages))
