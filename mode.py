from collections import Counter
import csv
with open("data.csv",newline="") as f:
    reader=csv.reader(f)
    fileData=list(reader)

fileData.pop(0)
newData=[]
for i in range(len(fileData)):
    num=fileData[i][2]
    newData.append(float(num))

data = Counter(newData)
modeDataRange={
    "90-100":0,
    "100-110":0,
    "110-120":0,
    "120-130":0,
    "130-140":0,
    "140-150":0,
    "150-160":0,
}
for weight,occurance in data.items():
    if 90<float(weight)<100:
        modeDataRange["90-100"]+=occurance
    elif 100<float(weight)<110:
        modeDataRange["100-110"]+=occurance
    elif 110<float(weight)<120:
        modeDataRange["110-120"]+=occurance
    elif 120<float(weight)<130:
        modeDataRange["120-130"]+=occurance
    elif 130<float(weight)<140:
        modeDataRange["130-140"]+=occurance
    elif 140<float(weight)<150:
        modeDataRange["140-150"]+=occurance
    elif 150<float(weight)<160:
        modeDataRange["150-160"]+=occurance


mode_range, mode_occurence = 0, 0
for range, occurence in modeDataRange.items():
    if occurence > mode_occurence:
        modeRange, modeOccurance = [int(range.split("-")[0]), int(range.split("-")[1])], occurance
mode = float((modeRange[0] + modeRange[1]) / 2)
print(mode)