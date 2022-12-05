#A Rock ; B Paper ; C Scissors
#X Rock ; Y Paper ; Z Scissors
#1        2         3
# 0 per perdita, 3 per pareggio, 6 per vittoria

def getValue(x):
    if x == 'A':
        return 1
    if x == 'B':
        return 2
    return 3

def getPoints(sfidante, io):
    if io == 'X':#LOSE
        if sfidante == 'A': 
            return getValue('C')
        if sfidante == 'B': 
            return getValue('A')
        return getValue('B')
    if io == 'Z':#WIN
        if sfidante == 'A': 
            return 6 + getValue('B')
        if sfidante == 'B': 
            return 6 + getValue('C')
        return 6 + getValue('A')
    return 3 + getValue(sfidante)

f = open('input.txt', 'r')
s = f.read().split('\n')
points = 0
for el in s:
    points += getPoints(el[0], el[2])
print(points)