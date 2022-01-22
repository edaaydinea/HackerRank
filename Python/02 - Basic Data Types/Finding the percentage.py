if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        student_marks[line[0]] = list(map(float, line[1:]))
    print('%.2f'.format(sum(student_marks[input()]) / 3))
