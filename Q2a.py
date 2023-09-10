import csv
from alignment.sequence import Sequence
from alignment.vocabulary import Vocabulary
from alignment.sequencealigner import SimpleScoring, GlobalSequenceAligner
import blosum as bl

keys=bl.BLOSUM(62)

file = open("Protein.txt", "r")

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

compare = open("BLOSSOM62.txt", "r")

compare_matrix = [[0 for x in range(23)] for x in range(30)]
line = compare.readline()
for i in range(30): 
    line = compare.readline()
    compare_matrix[i]=line.split()

for j in compare_matrix:
    del j[0]
for i in range(6):   
    del(compare_matrix[0])  

def score(a,b):
    x=Sequence(a)
    y=Sequence(b)

    scoring = SimpleScoring(1, 0)     #1 for +1 score , 0 for no gap penalty
    aligner = GlobalSequenceAligner(scoring, 0)

    v = Vocabulary()
    aEncoded = v.encodeSequence(x)
    bEncoded = v.encodeSequence(y)
    score,encodeds = aligner.align(aEncoded, bEncoded, backtrace=True)
    xx=0
    temp = ""
    for i in encodeds:
        alignment = v.decodeSequenceAlignment(i)
        if(xx<alignment.percentIdentity()):
            temp = alignment
    scorerr = 0
    for i in range(len(temp)):
        tempp1 = temp[i][0]
        tempp2 = temp[i][1]
        if(temp[i][0]=="-"):
            tempp1="*"
        if(temp[i][1]=="-"):
            tempp2="*"
        tempp = "" + tempp1 + tempp2
        scorerr = scorerr + keys[tempp]
    return -1*scorerr

distance_matrix = [[0 for i in range(10)] for j in range(10)]

for i in range(10):
    distance_matrix[i][i] = float("inf")
    for j in range(i+1,10):
        distance_matrix[i][j] = score(storage_matrix[i],storage_matrix[j])
        distance_matrix[j][i] = float("inf")

output_file = open("Pdistance.txt", "w")

write = csv.writer(output_file)
for i in range(10):
    write.writerow(distance_matrix[i])

output_file.close()