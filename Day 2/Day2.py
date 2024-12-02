def data():
    data=[]
    with open("Day 2/Day2-Data.txt") as file:
        for line in file: data.append(line.split())
    return data

def isSafe(line):
    amounts=[int(line[i])-int(line[i+1]) for i in range(len(line)-1)]
    if all(item in [1,2,3,-1,-2,-3] for item in amounts) and (all(item>0 for item in amounts) or all(item<0 for item in amounts)):
        return 1    
    else:
     return 0

def isDampSafe(line):
    amounts=[int(line[i])-int(line[i+1]) for i in range(len(line)-1)]
    if all(item in [1,2,3,-1,-2,-3] for item in amounts) and (all(item>0 for item in amounts) or all(item<0 for item in amounts)):
        return 1    
    else:
        for i in range(len(line)):
            altLine=line[::]
            altLine.pop(i-1)
            if isSafe(altLine):
                return 1
        return 0

part1,part2=0,0
for line in data():
    part1+=isSafe(line)
    part2+=isDampSafe(line)

print(f"Part1: {part1}\nPart2: {part2}")