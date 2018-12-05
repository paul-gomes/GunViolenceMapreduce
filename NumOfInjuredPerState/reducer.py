
o = open("./result/readyForReducer.txt", "r")
r = open("./result/result.csv", "w")

totalNumberInjured = 0
oldKey = None


# output column headers
r.write('state,NumberInjured\n')
 
for line in o:
    # use the line strip and split methods and assign to a list named data
    data_mapped = line.strip().split("\t")

    if len(data_mapped) != 2:
        continue
    thisKey, thisNumberInjured = data_mapped

    if oldKey and oldKey != thisKey:
        # output the last key value pair result
        r.write(thisKey + ',' + str(totalNumberInjured)+'\n')
        
        oldKey = thisKey
        totalNumberInjured = 0

    oldKey = thisKey
    totalNumberInjured += long(thisNumberInjured)

if oldKey != None:
    # output the final entry when done
    r.write(thisKey + ',' + str(totalNumberInjured)+'\n')
        

