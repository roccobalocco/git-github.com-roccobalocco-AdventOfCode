f = open('./Uno/input.txt', 'r')

l = list()
for el in f.read().split('\n\n'):
    tmp = 0
    for num in el.split('\n'):
        tmp += int(num)
    l.append(tmp)
l.sort(reverse=True)
print(sum(l[:3]))

#[ el for el in lista if el != "" ] 

