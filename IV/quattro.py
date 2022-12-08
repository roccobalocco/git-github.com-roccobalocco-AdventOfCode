def overlapse(uno, due):
    uno, due = uno.split('-'), due.split('-')
    if int(uno[0]) > int(due[0]): #due contiene uno
        if int(uno[1]) <= int(due[1]):
            return 1
    elif int(uno[0]) < int(due[0]): #uno contiene due
        if int(uno[1]) >= int(due[1]):
            return 1
    else:
        if int(uno[1]) >= int(due[1]):
            return 1
        elif int(uno[1]) <= int(due[1]):
            return 1
    return 0

def overlapseInterval(uno, due):
    uno, due = uno.split('-'), due.split('-')
    if int(uno[0]) > int(due[0]):            #due inizia prima 
        if int(due[1]) >= int(uno[0]):
            return 1
    elif int(uno[0]) < int(due[0]):          #uno inizia prima 
        if int(uno[1]) >= int(due[0]):
            return 1
    else:
        return 1
    return 0

def main(f):
    tot = 0
    l = f.read().split('\n')
    for el in l:
        tot += overlapseInterval(el.split(',')[0], el.split(',')[1])

    return tot

f = open("in.txt", "r")
print(main(f))