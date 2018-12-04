import csv

o = open("./result/readyForReducer.txt", "r")
s = open("./result/result.txt", "w")

totalNumberKilled = 0
oldKey = None



with open('./result/result.txt', 'wb') as csvfile:
    fieldnames = ['State', 'Num_of_persons_killed']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    #writer.writeheader()
 
    for line in o:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            continue
        thisKey, thisNumberKilled = data_mapped

        if oldKey and oldKey != thisKey:
            writer.writerow({'State': oldKey, 'Num_of_persons_killed': totalNumberKilled})
            oldKey = thisKey
            totalNumberKilled = 0

        oldKey = thisKey
        totalNumberKilled += long(thisNumberKilled)

    if oldKey != None:
        writer.writerow({'State': oldKey, 'Num_of_persons_killed': totalNumberKilled})

