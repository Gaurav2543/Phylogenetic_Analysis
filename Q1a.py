import csv
from alignment.sequence import Sequence
from alignment.vocabulary import Vocabulary
from alignment.sequencealigner import SimpleScoring, GlobalSequenceAligner

file = open("Nucleotide.txt", "r")

storage_matrix = [""]

k = 0
for i in range(10):
    line = file.readline()
    while(1):
        char = file.read(1)
        if(char == '' or char == '>'):
            storage_matrix.append("")
            k=k+1
            break
        if(char != '\n'):
            storage_matrix[k]=storage_matrix[k]+char
            
file.close()

def score(a,b):
    x=Sequence(a)
    y=Sequence(b)
    
    scoring = SimpleScoring(1, 0)     #1 for +1 score , 0 for no gap penalty
    aligner = GlobalSequenceAligner(scoring, 0)

    v = Vocabulary()
    aEncoded = v.encodeSequence(x)
    bEncoded = v.encodeSequence(y)
    score,encodeds = aligner.align(aEncoded, bEncoded, backtrace=True)
    matrix=[]
    for i in encodeds:
        alignment = v.decodeSequenceAlignment(i)
        matrix.append(alignment.percentIdentity())
    temp = max(matrix)
    matrix=[]
    return 100-temp

distance_matrix = [[0 for i in range(10)] for j in range(10)]

for i in range(10):
    distance_matrix[i][i] = 'inf'
    for j in range(i+1,10):
        distance_matrix[i][j] = score(storage_matrix[i],storage_matrix[j])
        distance_matrix[j][i] = 'inf'

output_file = open("Ndistance.txt", "w")

write = csv.writer(output_file)
for i in range(10):
    write.writerow(distance_matrix[i])

output_file.close()