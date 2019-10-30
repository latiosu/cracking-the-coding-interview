# Example: A ransom note can be formed by cutting words out of a magazine to form a new
# sentence. How would you figure out if a ransom note (represented as a string) can be
# formed from a given magazine (string)?

# Interpretation: Design an algorithm that checks if a list of strings m contains all
# occurrances of another list of strings n. If it does, return true, otherwise false.

import re

def canFormRansomNote(note, magazine):
    if len(note) > len(magazine):
        return False

    regexDelimiters = r'[,. ]'

    # Build a word count from magazine
    magazineMap = buildWordCount(re.split(regexDelimiters, magazine))

    # Build a word count from note
    noteMap = buildWordCount(re.split(regexDelimiters, note))

    # Check if all note word counts fit into magazine word counts
    for word in list(noteMap):
        if word not in magazineMap or magazineMap[word] < noteMap[word]:
            return False

    # All word counts are accounted for and match
    return True

def buildWordCount(stringList):
    wordCount = {}
    for word in stringList:
        if word not in wordCount:
            wordCount[word] = 1
        else:
            wordCount[word] += 1
    return wordCount

print(canFormRansomNote("sinister group lurking at holiday", \
    "There’s a sinister problem lurking in many workplaces \
    putting people at risk, and one group thinks the way to tackle it is with a \
    new public holiday."))

print(canFormRansomNote("sinister group will kill", \
    "There’s a sinister problem lurking in many workplaces \
    putting people at risk, and one group thinks the way to tackle it is with a \
    new public holiday."))