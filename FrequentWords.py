
def BetterFrequentWords (text, k):
    frequentPatterns = []
    frequentPatternsMap = {}
    
    textLength = len(text)
    
    for i in range(0, textLength-k+1):
        pattern = text[i: i+k]
        
        if pattern in frequentPatternsMap:
            frequentPatternsMap[pattern] = frequentPatternsMap[pattern] + 1
        else:
            frequentPatternsMap[pattern] = 1
        
    maxFrequency = max(frequentPatternsMap.values())
    
    for pattern in frequentPatternsMap:
        if frequentPatternsMap[pattern] == maxFrequency:
            frequentPatterns.append(pattern)
    
    return frequentPatterns

DNAString = "ACGTTTCACGTTTTACGG"
k = 3

frequentWordsInDNA = BetterFrequentWords(DNAString, k)
print(frequentWordsInDNA)



