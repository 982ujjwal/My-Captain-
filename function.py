def most_frequent(string):
    D=dict()
    for i in string:
        if i in D:
            D[i]+=1
            
        else:
            D[i]=1
    return D
print (most_frequent("Missippi"))