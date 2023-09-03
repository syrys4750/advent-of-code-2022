file = open('adventofcode.com_2022_day_3_input.txt', 'r')
# file = open('demo.txt', 'r')
sacks = file.readlines()
currentSackItems = {}
totalPriority = 0
firstSack = ''
secondSack = ''
thirdSack = ''

def itemValue(item):
    if item.islower():
        return ord(item) - 96
    return ord(item) - 64 + 26

def findRepeated(firstSack, secondSack, thirdSack):
    for item in firstSack:
        currentSackItems[item] = 0
    for item in secondSack:
        if item in currentSackItems:
            currentSackItems[item] = 1
    for item in thirdSack:
        if item in currentSackItems and currentSackItems[item] == 1:
            currentSackItems.clear()
            return itemValue(item)

for sack in sacks:
    sack.replace('\n', '')
    print(sack)
    if firstSack == '':
        firstSack = sack
    elif secondSack == '':
        secondSack = sack
    elif thirdSack == '':
        thirdSack = sack
    
    if firstSack != '' and secondSack != '' and thirdSack != '':
        totalPriority = totalPriority + findRepeated(firstSack, secondSack, thirdSack)
        firstSack = ''
        secondSack = ''
        thirdSack = ''

print(totalPriority)
