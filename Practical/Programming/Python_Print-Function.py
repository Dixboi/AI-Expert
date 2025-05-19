'''
https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true
'''

def function(n: int) -> str:
    return [print(str(i+1), end="") for i in range(n)]

if __name__ == '__main__':
    n = int(input())
    function(n)
