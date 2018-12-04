# reader = open("googleplaystore.csv", "r")
# writer = open("mapperOutput.txt", "w")
# line_count = 1
# for line in reader:
#     datalist = line.strip().split(",")
#     if (len(datalist) == 13):
#         if line_count != 1:
#             app, category, rating, reviews, size, installs, type, price, contentRating, genres, lastUpdated, currentVer, AndroidVer = datalist
#             price = price.replace("$", "")
#             installs = installs.replace("+", "").replace(",", "")
#             writer.write(price + "\t" + installs + "\n")
#         line_count += 1

# reader.close()
# writer.close()

import csv

c = open("result/mapperOutput.txt", "w")

with open("../dataset/gun-violence-data.csv", "rb") as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    line_count = 0;
    for row in reader:
        if (line_count != 0):
            if (len(row) == 29):
                state = row[2].replace("$", "")
                numberOfKilled = row[5]
                c.write(state + "\t" + numberOfKilled + "\n")
        line_count += 1

c.close()

