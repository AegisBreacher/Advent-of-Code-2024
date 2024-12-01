def data():
    list1,list2=[],[]
    with open("Day 1/Day1-Data.txt","r") as file:
        for line in file:
            line=line.split()
            list1.append(line[0])
            list2.append(line[1])
    return list1,list2

def findSimilarity(list1,list2,score=0):
    for i in list1:
        score+=int(i)*list2.count(i)
    return score

list1,list2=data()
print(findSimilarity(list1,list2))