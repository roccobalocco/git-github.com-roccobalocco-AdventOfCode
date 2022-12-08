def createStacks(s):
    st = list()
    for i in range(0, 9):
        st.append(list())
    for el in s:
        tmp = 3
        cnt = 0
        while(tmp < 35):
            cargo = el[tmp-3:tmp]
            if cargo != "   ":
                st[cnt].append(cargo[1:2])
            tmp += 4
            cnt += 1
        cargo = el[-3:]
        if cargo != "   ":
            st[cnt].append(cargo[1:2])
    for i in range(0,  9):
        st[i].reverse()
    return st

def move(ist, st):
    ist = ist.split(' ')
    toMove, f, t = int(ist[1]), int(ist[3]), int(ist[5])
    if toMove == 1:
        st[t-1].append(st[f-1].pop())
    else:
        tmp = list()
        for i in range(0, toMove):
            tmp.append(st[f-1].pop())
        while len(tmp) > 0:
            st[t-1].append(tmp.pop())
    return st

def main(f):
    inp = f.read().split('\n\n')[:8]
    st = inp[0].split('\n')[:8]
    ist = inp[1].split('\n')
    st = createStacks(st)
    for i in range(1, 10):
        print(i, "-->", st[i-1])
    for i in ist:
        st = move(i, st)
    return st

f = open('in.txt', 'r')
tops = main(f)
s = ""
for top in tops:
    s += top.pop()
print(s)