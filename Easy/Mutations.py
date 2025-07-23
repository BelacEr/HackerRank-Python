# Problem: Mutations
# Difficulty: Easy
# Points: 10.00 points
# URL: https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true

def mutate_string(string, position, character):
    new_string = string
    l = list(new_string)
    l[position] = character
    string = ''.join(l)
    
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)