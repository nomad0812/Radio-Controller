def getStationList(fileName):

    stations = []

    statFile = open(fileName)
 
    for line in statFile:
        row = line.split(': ')
        #this is done to the list index is within range
        #row.append('')
        stations.append(row)

    statFile.close()

    return stations

STATS = getStationList("radio_stations.txt")

for i in STATS:
    print i
