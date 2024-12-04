def data():
    data=[]
    with open("Day 4/Day4-Data.txt","r") as f:
        for line in f.readlines():
            data.append(line.strip())
    return data

def findXMAS(data,x,y,searchWord,found=0):
    for dirX,dirY in ((0,1),(0,-1),(1,0),(1,1),(1,-1),(-1,0),(-1,1),(-1,-1)):
        word=""
        for i in range(len(searchWord)):
            searchX=x+(i*dirX)
            searchY=y+(i*dirY)
            if not searchY in range(len(data)) or not searchX in range(len(data[0])):
                break
            word+=data[searchY][searchX]
        if word==searchWord:
            found+=1
    return found

data=data()
part1,part2=0,0
for y in range(len(data)):
    for x in range(len(data)):
        part1+=findXMAS(data,x,y,"XMAS")
        if data[y][x]=="A":
            if y+1 not in range(len(data)) or y-1 not in range(len(data)) or x-1 not in range(len(data[0])) or x+1 not in range(len(data[0])):
                pass
            elif data[y+1][x-1] + data[y-1][x+1] in ["MS","SM"] and data[y-1][x-1] + data[y+1][x+1] in ["MS","SM"]:
                part2+=1

print(f"Part1: {part1}\nPart2: {part2}")