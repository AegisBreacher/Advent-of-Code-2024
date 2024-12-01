def data():
    list1,list2=[],[]
    with open("Day 1/Day1-Data.txt","r") as file:
        for line in file:
            line=line.split()
            list1.append(line[0])
            list2.append(line[1])
    return list1,list2

def findMins(list1,list2,score=0):
    while len(list1)>0:
        score+=abs(int(min(list1))-int(min(list2)))
        list1.remove(min(list1))
        list2.remove(min(list2))
    return score

def findSimilarity(list1,list2,score=0):
    for i in list1:
        score+=int(i)*list2.count(i)
    return score

list1,list2=data()
#Ordered this way as to not mess up the part 2 with part 1's removal of items
print(findSimilarity(list1,list2))
print(findMins(list1,list2))