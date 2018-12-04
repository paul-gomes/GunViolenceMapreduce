
o = open("./result/readyForReducer.txt", "r")
r = open("./result/result.csv", "w")

totalNumOfIncidents = 0
oldKey = None


# output column headers
r.write('State, TotalNumOfIncidents\n')
 
for line in o:
    # use the line strip and split methods and assign to a list named data
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 2:
        continue
    thisKey, numOfIncident = data_mapped

    if oldKey and oldKey != thisKey:
        # output the last key value pair result
        r.write(thisKey + ',' + str(totalNumOfIncidents)+'\n')
        
        oldKey = thisKey
        totalNumOfIncidents = 0

    oldKey = thisKey
    totalNumOfIncidents += long(numOfIncident)

if oldKey != None:
    # output the final entry when done
    r.write(thisKey + ',' + str(totalNumOfIncidents)+'\n')
        

