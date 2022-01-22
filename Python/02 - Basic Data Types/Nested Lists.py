if __name__ == '__main__':
    score_list = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())

        if score in score_list:
            score_list[score].append(name)
        else:
            score_list[score] = [name]

    name_list = []

    for i in score_list:
        name_list.append([i, score_list[i]])
        name_list.sort()
    result = name_list[1][1]
    result.sort()
    print(*result, sep="\n")
