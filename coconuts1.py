 # Write program that will find the initial number
 #of coconuts. 

def f(n):
    return (n-1) / 5.0 * 4

def f6(n):
    for i in range(6):
        n = f(n)
    return n 

def is_int(n):
    return abs(n-int(n)) < 0.0000001
                               
for n in range(20000):
    if is_int(f6(n)):
        print n

