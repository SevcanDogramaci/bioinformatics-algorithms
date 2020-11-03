# bioinformatics-algorithms

The algorithms implemented in the extend of CENG 4217 Bioinformatics Algorithms course.<br>
Pseudocodes are as follows.

~~~
BetterFrequentWords(text, k)
  freqPatterns = an empty array
  freqMap = empty map
  n = len(text)
  
  for every integer i between 0 and n - k
    pattern = text[i, i+k]
    if freqMap[pattern] doesn’t exist
      freqMap[pattern] = 1
    else
      freqMap[pattern] = freqMap[pattern] + 1
      
  maxCount = MaxMap(freqMap)
  
  for all strings pattern in freqMap
    if freqMap[pattern] = maxCount
      freqPatterns = Append(freqPatterns, pattern)
      
  return freqPatterns
~~~

~~~
GibbsSampler(Dna, k, t, N)
  randomly select k-mers Motifs = (Motif1, ..., Motift ) from Dna
  BestMotifs ← Motifs
  
  for j ← 1 to N 
    i ← randomly generated integer between 1 and t
    Profile ← profile formed from all Motifs other than Motifi
    Motifi ← Profile-randomly generated k-mer in Dnai
    if Score(Motifs) < Score(BestMotifs)
      BestMotifs ← Motifs
      
 return BestMotifs
~~~
