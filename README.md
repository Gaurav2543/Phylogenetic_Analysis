# Phylogenetic analysis

## Problem Statements

### Part 1:
Construct a phylogenetic relationship for the given nucleotide sequences (Nucleotide.txt).
a. Write a script to generate a distance matrix csv file for the sequences present in the
data file. Name the distance matrix file as 'Ndistance.txt'.
For example,
seq1 = 'ATGCATGCAA'
seq2 = 'ATGCATGCTA'
Distance (seq1, seq2) = Mismatches/total length = 1/10 = 0.1
b. Write a script that uses 'Ndistance.txt' and generate phylogenetic relationship
between the organisms using UPGMA method.

## Explanation of my Solution
Please ensure that the ".txt" files are in the same folder as relative path is given. Some libraries need to be installed for appropriate working.
I have made the distance matrix. It takes about 40 seconds for program to complete, so you might have to wait for some time for the output after execution of the program. The progam takes the input from the file "Nucleotide.txt". The output tree has been drawn by hand along with the distances being specified alongside and the image has been uploaded as "Tree1.jpeg" based on the output of the program, stored in the file "Ndistance.txt".


### Part 2:
Construct a phylogenetic relationship for the given protein sequences (Protein.txt).
a. Write a script to generate a distance matrix csv file for the sequences present in the
data file. Name the distance matrix file as 'Pdistance.txt'. Use BLOSUM62 for getting score
values.
b. Write a script that uses 'Pdistance.

## Explanation of my Solution
Please ensure that the ".txt" files are in the same folder as relative path is given. Some libraries need to be installed for appropriate working.
I have made the closeness matrix (i.e. the closer the proteins are, more their score). The progam takes the input from the file "Protein.txt". The output tree has been drawn by hand along with the distances being specified alongside and the image has been uploaded as "Tree2.jpeg" based on the output of the program, stored in the file "Pdistance.txt". The reference used for the calculation in this program is the BLOSUM62 distance matrix, which is present as "BLOSUM62.txt". The orientation of the tree is different than the one in Part1 since the closeness matrix indicates score and not the distance.
