# Problem: Print Function
# Difficulty: Easy
# Points: 20.00 points
# URL: https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    result = ""
    for i in range(1, n+1):
        result += str(i)
    print(result)