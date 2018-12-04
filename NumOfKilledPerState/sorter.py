o = open("./result/mapperOutput.txt", "r")
s = open("./result/readyForReducer.txt", "w")

lines = o.readlines()
lines.sort()

for line in lines:
  s.write(line)

o.close()
s.close()