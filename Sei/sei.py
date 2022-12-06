from collections import Counter
def checkDuplicate(s): #first Part
    els = Counter(s)
    return len([k for k,v in els.items() if v > 1]) != 0

def main2(f):
    mark = 0
    s = f.read()
    for i in range(13, len(s)):
        if not checkDuplicate(s[i-13:i+1]):
            mark = i + 1
            break
    return mark

def main(f):
    mark = 0
    s = f.read()
    for i in range(3, len(s)):
        if not checkDuplicate(s[i-3:i+1]):
            mark = i + 1
            break
    return mark


f = open('in.txt', 'r')
#print(main(f))
print(main2(f))