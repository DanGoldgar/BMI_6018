# Dan Goldgar u0414652
# Advanced Functions and Logic: while_inner_plus

# Test Cases
complexList = [1,2,3,[4,5,[6,7],8],9,[10,11,[12,13]]]
simpleList = [1,2,3]
easyList = [1,2,3,[4,5]]
doubleList = [[1,2],[3,4]]

# Function finds the deepest list in a nested list, adds 1 to each value, returns list
# If multiple lists are found at same depth, function adds to each value, returns list of deepest lists
def while_inner_plus(testList):
    lowList = []
    trackingList = []
    subList = []
    addList = []
    outList = []
    hasList = True
    multList = False

    # Loops through list at least once, continues if list contains another list
    # multList checks if multiple lists are found in list at this depth
    while hasList:
        hasList = False
        i = 0
        while i < len(testList):
            if isinstance(testList[i], list):
                lowList.append(testList[i])
                subList.extend(testList[i])
                if hasList:
                    multList = True
                hasList = True
            i += 1
        if hasList:
            # trackingList keeps track of list structure at depth n-1 in case of multiple lists at equal depth
            trackingList = lowList.copy()
            testList = subList.copy()
            subList.clear()
            lowList.clear()

    # This code takes the list of deepest lists contained in trackingList, adds one to each element,
    # and reconstructs the nested list in case of multiple lists at equal depth
    if multList:
        j = 0
        while j < len(trackingList):
            tempList = trackingList[j]
            for x in tempList:
                addList.append(x + 1)
            outList.append(addList.copy())
            addList.clear()
            j += 1
        return outList
    # Simple case, single list at max depth
    else:
        for x in testList:
            outList.append(x + 1)
        return outList

print(while_inner_plus(doubleList))