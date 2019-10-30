# Example: Design an algorithm to print all permutations of a string.
# For simplicity, assume all characters are unique.

def permutations(string):
    # Base cases
    if len(string) <= 1:
        return [string]
    if len(string) == 2:
        return [string, string[1] + string[0]]

    # Recursive case
    results = []
    lastChar = string[-1]

    # Insert last character into every position of permutations(string[:-1])
    for permutation in permutations(string[:-1]):
        for i in range(len(permutation)):
            results.append(permutation[0:i] + lastChar + permutation[i:len(permutation)])
    return results

print(permutations("abcdef"))