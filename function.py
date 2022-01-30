import operator


def most_frequent(string):
    D=dict()
    for i in string:
        if i in D:
            D[i]+=1
            
        else:
            D[i]=1
        sorted_dict = dict( sorted(D.items(), key=operator.itemgetter(1),reverse=True))
        
    return sorted_dict
print (most_frequent("Mississippi"))
