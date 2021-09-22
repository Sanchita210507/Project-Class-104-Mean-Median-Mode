import csv
with open("data.csv",newline="") as f:
    reader=csv.reader(f)
    fileData=list(reader)

fileData.pop(0)
newData=[]
for i in range(len(fileData)):
    number=fileData[i][2]
    newData.append(float(number))
n=len(newData)
total=0

for s in newData:
    total=total+s

mean=total/n

print(mean)
