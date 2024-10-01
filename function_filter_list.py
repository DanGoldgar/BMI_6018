# This function takes a list and a threshold as arguments and returns a list with values below threshold
def filter_list(userList,threshold):
    outputList = []
    for x in userList:
        if x <= threshold:
            outputList.append(x)
    return outputList

testList = [0,1,2,3,4,5,6]
print(filter_list(testList, 3))