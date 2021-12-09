# Author: SCT (AMDG) 12/9/21

def totalpoints(freethrow, twopoint, threepoint):
    totalpoints = 0
    totalpoints = (1 * freethrow) + (2 * twopoint) + (3 * threepoint)
    return totalpoints



print(totalpoints(3,2,1))

print(totalpoints(1,2,3))

print(totalpoints(1,1,1))



