from random import randint
import copy 

def generateRandomDNA(DNASequenceCount, nucleotidePerSequence):
    
    nucleotides = ['a', 't', 'g', 'c']
    DNA= ""
    
    for i in range(0, DNASequenceCount):
        sequence = ""
        
        for j in range(0, nucleotidePerSequence):
            randomIndex = randint(0, len(nucleotides)-1)
            sequence += nucleotides[randomIndex]
        DNA += sequence
    return DNA

def selectRandomMotifsFromDNA(DNA, k, t):
    DNASequenceCount = (int)(len(DNA) / t)
    Motifs = []
    
    for i in range(0, DNASequenceCount):
        startOfSequence = (i*t)
        endOfSequence = (i*t)+t
        sequence = DNA[startOfSequence: endOfSequence]
        
        randomStartOfMotif = randint(0, t-k)
        Motifs.append(sequence[randomStartOfMotif: (randomStartOfMotif+k)])

    return Motifs

def generateProfileMatrix(Motifs, randomMotifIndexToRemove):
    
    k = len(Motifs[0])
    DNASequenceCount = len(Motifs)
    Profile = [{base: 0 for base in "atgc"} for j in range(k)]
    ProfileNeedToPseudocounts = False
    
    for j in range(0, k):
        for i in range(0, DNASequenceCount):
            if i != randomMotifIndexToRemove:
                character = Motifs[i][j]
                if(character in Profile[j]):
                    (Profile[j])[character] += 1
        
        if(not ProfileNeedToPseudocounts and 0 in Profile[j].values()):
            ProfileNeedToPseudocounts = True
                
    return (Profile, ProfileNeedToPseudocounts)

def updateProfileMatrix(Profile, k, addPseudocounts):
    
    for column in Profile:
        for base in column:
            if addPseudocounts:
                column[base] += 1
                column[base] /= (2*k)
            else:
                column[base] /= k
    return Profile

def Score(Motifs):
    
    k = len(Motifs[0])
    Profile = [{base: 0 for base in "atgc"} for j in range(k)]
    DNASequenceCount = len(Motifs)
    Score = 0
    
    for j in range(0, k):
        for i in range(0, DNASequenceCount):
            character = Motifs[i][j]
            if(character in Profile[j]):
                (Profile[j])[character] += 1
        Score += DNASequenceCount - max(Profile[j].values())
    return Score

def findMostProbableKmerInRemovedDNASequence(RemovedDNASequence, Profile, k):
    
    mostProbableKmer = None
    mostProbableKmerProbability = None
    
    for i in range(0, len(RemovedDNASequence)-k+1):
        kmer = RemovedDNASequence[i:(i+k)]
        probabilityOfKmer = 1
        
        for j in range(0, k):
            probabilityOfKmer *= (Profile[j][(kmer[j])])
        
        if mostProbableKmerProbability is None or probabilityOfKmer > mostProbableKmerProbability:
            mostProbableKmerProbability = probabilityOfKmer
            mostProbableKmer = kmer
    return mostProbableKmer

def GibbsSampler(DNA, k, t, N):
    
    Motifs = selectRandomMotifsFromDNA(DNA, k, t)
    BestMotifs = copy.deepcopy(Motifs)
    
    for j in range(0, N):
        randomMotifIndexToRemove = randint(0, len(Motifs)-1)
        Profile, addPseudocounts = generateProfileMatrix(Motifs, randomMotifIndexToRemove)
        
        Profile = updateProfileMatrix(Profile, len(Motifs)-1, addPseudocounts)
            
        startOfSequence = (randomMotifIndexToRemove*t)
        endOfSequence = (randomMotifIndexToRemove*t)+t
        RemovedDNASequence = DNA[startOfSequence: endOfSequence]
        
        MostProbableKmer = findMostProbableKmerInRemovedDNASequence(RemovedDNASequence, Profile, k)
        Motifs[randomMotifIndexToRemove] = MostProbableKmer
        
        if Score(Motifs) < Score(BestMotifs):
           BestMotifs = copy.deepcopy(Motifs)
           
    return BestMotifs


DNA = generateRandomDNA(10, 100)
print(GibbsSampler(DNA, 5, 100, 10))



