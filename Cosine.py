def GetCos(List1,List2):
    if (len(List1)!= len(List2)):
        return -1
    i=0
    s=0
    for i in range(len(List1)):
       s = s + List1[i]*List2[i]
       i = i + 1

    return s
