# homework 1
# Complete the following code that the robot could
# localize in 2-D world. 

colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

#colors = [['green', 'green', 'green'],
#          ['green', 'red', 'red'],
#          ['green', 'green', 'green']]

measurements = ['green', 'green', 'green' ,'green', 'green']
#measurements = ['red', 'red']

# [0, 0] no motion;  [0, 1] move right
# [0,-1] move left;  [1, 0] move down
# [-1, 0] move up

motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
#motions = [[0,0],[0,1]]

sensor_right = 0.7
#sensor_right = 1.0

p_move = 0.8
#p_move = 0.5

def show(p):
    for i in range(len(p)):
        print p[i]


#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT

# generate uniform distribution according to the
# size of the colors
row = len(colors)
col = len(colors[1])
p = []
for i in range(row):
    p.append([])
    for j in range(col):
        p[i].append(1.0/(row*col))

# sense function
def sense(p, Z):
    q = []
    for i in range(len(p)):
        q.append([])
        for j in range(len(p[i])):
            hit = (Z == colors[i][j])
            q[i].append(p[i][j] * (hit * sensor_right + (1-hit) * (1-sensor_right)))
    # summation of each entry
    s = 0
    for i in range(len(q)):
        s += sum(q[i])
    
    # normalize
    for i in range(len(q)):
        for j in range(len(q[i])):
            q[i][j] = q[i][j] / s
    return q

# move function
def move(p, U):
    q = []
    for i in range(len(p)):
        q.append([])
        for j in range(len(p[i])):
            s = p[(i-U[0])%len(p)][(j-U[1])%len(p[i])]*p_move + \
                p[i][j] * (1 - p_move)
            q[i].append(s) 
    return q 

for i in range(len(measurements)):
    p = move(p, motions[i])
    p = sense(p, measurements[i])
   # p = move(p, motions[i])


#Your probability array must be printed 
#with the following code.

show(p)





