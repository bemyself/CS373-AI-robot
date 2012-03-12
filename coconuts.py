# coconuts.py - five people and a monkey stranded on an island, they collected a huge pile of coconuts and decided to separate them with five equal parts. However, one guy wanted to take away 1/5 but it is not divisible by 5, so he gave one coconut to the monkey. Then the second guy did the same thing, and so on. 

def is_int(n):
    return abs(n - int(n)) < 0.0000001

def left(x):
    return 4.0 * (x - 1)/5

def left6(x):
    for i in range(6):
       x = left(x)
    return x

for x in range(20000):
    if is_int(left6(x)):
        print x
