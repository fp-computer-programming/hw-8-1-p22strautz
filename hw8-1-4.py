# Author: SCT (AMDG) 12/9/21

def half(string):
    length = len(string)
    half_length = length // 2

    print(string[0:half_length])
    print(string[half_length:length])


half("racecars")
half("string")
half("nice")
