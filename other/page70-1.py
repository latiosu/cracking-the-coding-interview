# Example: Given a smaller string s and a bigger string b, design an algorithm to find all
# permutations of the shorter string within the longer one.
# Print the location of each permutation.

import collections

NUM_CHARS = 26

def printPermutationsLocations(string, bigString):
    print(bigString)
    # 1. Build array of required letter counts (order doesn't matter so we can use counts)
    requiredCount = [0] * NUM_CHARS
    for char in string:
        requiredCount[indexOf(char)] += 1

    # 2. Create variables for checking if permutation
    index = 0
    validCount = 0
    windowCount = [0] * NUM_CHARS
    queue = collections.deque()

    # 3. Scan big string for permutations of string
    for char in bigString:
        # Track rolling window and enforce window size to match search string
        queue.append(char)
        if len(queue) > len(string):
            removedChar = queue.popleft()
            # Check if we about to remove a valid character
            if  requiredCount[indexOf(removedChar)] > 0 \
                and windowCount[indexOf(removedChar)] <= requiredCount[indexOf(removedChar)]:
                validCount -= 1
            windowCount[indexOf(removedChar)] -= 1


        # Check if we found another valid character
        windowCount[indexOf(char)] += 1
        if requiredCount[indexOf(char)] > 0 \
            and windowCount[indexOf(char)] <= requiredCount[indexOf(char)]:
            validCount += 1
        
        # Check if our window is a valid permutation
        if validCount == len(string):
                printLocation(index, string, bigString)

        # Remember our index
        index += 1

def printLocation(endIndex, string, bigString):
    startIndex = endIndex - (len(string) - 1)
    spaces = " " * startIndex
    print(spaces + bigString[startIndex:endIndex + 1])

def indexOf(char):
    return ord(char.lower()) - ord("a")

printPermutationsLocations("abbc", "cbabadcbbabbcbabaabccbabc")