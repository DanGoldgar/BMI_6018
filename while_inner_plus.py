
inputList = [1,2,3,[4,5,[6,7],8],9,[10,11,[12,13]]]
simpleList = [1,2,3]
doubleList = [[1,2],[3,4]]

lowList = []
trackingList = []
hasList = True
subList = []

outList = []
outList2 = []

testList = list(inputList)
while hasList:
    hasList = False
    i = 0
    while i < len(testList):
        if isinstance(testList[i], list):
            lowList.append(testList[i])
            subList.extend(testList[i])
            hasList = True
        i += 1
    if hasList:
        trackingList = lowList.copy()
        testList = subList.copy()
        subList.clear()
        lowList.clear()
for x in testList:
    outList.append(x+1)
for x in trackingList[0]:
    outList2.append(x+1)
print(outList)
print(outList2)
