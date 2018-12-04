
import csv

c = open("result/mapperOutput.txt", "w")

with open("../dataset/gun-violence-data.csv", "rb") as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    line_count = 0;
    for row in reader:
        if (line_count != 0):
            if (len(row) == 29):
                state = row[2]
                c.write(state + "\t" + str(1) + "\n")
        line_count += 1

c.close()

