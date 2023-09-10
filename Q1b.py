import numpy as np
CSVData = open("Ndistance.txt")
dist_matrix = np.loadtxt(CSVData, delimiter=",")

new_matrix = []

for i in range(len(dist_matrix)):
    new_matrix.append([])
    for j in range(len(dist_matrix)):
        new_matrix[i].append(dist_matrix[i][j])

def findminindices(a):
    shortest_distance=min([min(r) for r in a])
    for i in range(len(a)):
        for j in range(len(a)):
            if(shortest_distance==a[i][j]):
                x=i
                y=j
    return x,y

def UPGMA(matrix):
    i=findminindices(matrix)[0]
    j=findminindices(matrix)[1]
    if(i<j):
        dist_from_tip=matrix[i][j]/2
        for k in range(len(matrix)):
            if (k<i):
                matrix[k][i]=(matrix[k][i]+matrix[k][j])/2
            if(k<j and k>i):
                matrix[i][k]=(matrix[i][k]+matrix[k][j])/2                    
            if(k>j):
                matrix[i][k]=(matrix[i][k]+matrix[j][k])/2                   
        for x in matrix:
            del x[j]                    
        del(matrix[j])
    return matrix,dist_from_tip

for i in range(len(new_matrix)-2):
    b=UPGMA(new_matrix)
    dist_from_tip=b[1]
#     print(dist_from_tip)     #shortest distance/2 of every matrix (that is distance from tip of the tree)

print(b)  #final matrix after applying UPGMA

total_length=b[0][0][1]/2
# print(total_length)     #total height of the tree
