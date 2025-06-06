'''
https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks = student_marks.get(query_name)
    avg = "{:.2f}".format(round(sum(marks) / len(marks), 2))
    print(avg)
