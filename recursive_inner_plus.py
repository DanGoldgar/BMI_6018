# Dan Goldgar u0414652
# Advanced Functions and Logic: recursive_inner_plus.py

# Test Cases
simpleList = [1,2,3]
easyList = [1,2,3,[4,[5,6]]]
complexList = [1,2,3,[4,5,[6,7],8],9,[10,11,[12,13]]]
doubleList = [[1,2],[3,4]]

# Function finds the deepest list in a nested list, adds 1 to each value, returns list
# If multiple lists are found at same max depth, function adds 1 to each value and returns list of values at depth
def recursive_inner_plus(testList):
    subList = []
    outList = []
    hasList = False

    # Check items for list type
    i = 0
    while i < len(testList):
        if isinstance(testList[i], list):
            subList.extend(testList[i])
            hasList = True
        i += 1
    # If list contains another list, function calls itself
    if hasList:
        recursive_inner_plus(subList)

    else:
        for x in testList:
                outList.append(x + 1)
        print(outList)
        return outList

recursive_inner_plus(simpleList)
