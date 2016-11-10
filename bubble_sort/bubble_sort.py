input = [3, 45, 23, 77, 43, 7, 10, 16, 39]

def sort(input):

    sortedInput = input
    temp = 0
    leftIndex = 0
    rightIndex = len(input)-1
    
    print sortedInput
    
    while rightIndex > 1:
        while leftIndex < rightIndex:
            print leftIndex
            if sortedInput[leftIndex] > sortedInput[leftIndex+1]:
                temp = sortedInput[leftIndex]
                sortedInput[leftIndex] = sortedInput[leftIndex+1]
                sortedInput[leftIndex+1] = temp
            leftIndex += 1
        leftIndex = 0
        rightIndex -= 1
        print sortedInput
        
sort(input)