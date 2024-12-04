import re

def data():
    with open("Day 3/Day3-Data.txt","r") as f: return f.read()

def part1(data=data(),score=0):
    for item in re.findall(r"mul\(\d\d?\d?,\d\d?\d?\)",data):
        numlist=re.findall(r"\d\d?\d?",item)
        score+=int(numlist[0])*int(numlist[1])
    return score

def part2(data=data(),score=0):
    do=True
    for item in re.findall(r"mul\(\d\d?\d?,\d\d?\d?\)|do\(\)|don't\(\)",data):
        if item=="do()":
            do=True
            next
        elif item=="don't()":
            do=False
            next
        elif do:
            numlist=re.findall(r"\d\d?\d?",item)
            score+=int(numlist[0])*int(numlist[1])
    return score

print(f"Part1: {part1()}\nPart2: {part2()}")