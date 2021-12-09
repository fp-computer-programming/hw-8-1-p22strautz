# Author: SCT (AMDG) 12/9/21

def palindrome(word):
    if word == word[:: -1]:
        print("The word {0} is a palindrome because {0} spelled backwards is {0}.".format(word))
    else:
        print("The word {0} is not a palindrome because {0} spelled backwards is " + word[:: -1] + ".".format(word))


palindrome("racecar")
palindrome("hat")
palindrome("bob")
