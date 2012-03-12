a = [[31, 92, 43],
     [23, 15, 0]]

motion = [0,-1]

def tdmove(p, U):
    q = []
    for i in range(len(a)):
        q.append([])
        for j in range(len(a[i])):
            q[i].append(p[(i-U[0])%len(a)][(j-U[1])%len(a[i])])
    return q

p = tdmove(a, motion)
print p
