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
    return matrix

for i in range(len(new_matrix)-2):
    b=UPGMA(new_matrix)

print(b)   #final matrix after applying UPGMA
