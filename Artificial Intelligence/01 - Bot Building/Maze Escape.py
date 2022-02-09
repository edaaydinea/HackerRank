def writeMap(view, name):
    f = open(name, 'w')
    for i in range(0, len(view)):
        view[i] = view[i] + '\n'
    f.writelines(view)
    f.close()


def writePrev(output):
    f = open('prev.dat', 'a+')
    f.write(output + '\n')
    f.close()
    return output


def nextMove(view):
    target = []
    for i in range(0, len(view)):
        if 'e' in view[i]:
            target = [view[i].index('e'), i]
            if target[0] == 0:
                return "LEFT"
            elif target[0] == 2:
                return "RIGHT"
            elif target[0] == 1:
                return "UP"
        if '-' in view[i]:
            for j in range(view[i].index('-'), 3):
                if i == 1 and j == 1: j += 1
                if '-' in view[i][j:]: target.append([view[i].index('-', j), i])

    f = open('prev.dat', 'a+')
    f.close()
    f = open('prev.dat', 'r')
    pMoves = f.readlines()
    f.close()
    f = open('prevMap.dat', 'a+')
    f.close()
    f = open('prevMap.dat', 'r')
    pMap = f.readlines()
    f.close()
    f = open('prevMap2.dat', 'a+')
    f.close()
    f = open('prevMap2.dat', 'r')
    pMap2 = f.readlines()

    for i in range(0, len(pMap)):
        pMap[i] = pMap[i].replace('\n', '')
    for i in range(0, len(pMap2)):
        pMap2[i] = pMap2[i].replace('\n', '')

    # remove duplicates
    dup = target
    target = []
    [target.append(x) for x in dup if x not in target]

    if len(pMoves) < 3 and len(target) == 3:
        if [0, 1] in target and [1, 2] in target:
            writeMap(view, 'prevMap.dat')
            writeMap(pMap, 'prevMap2.dat')
            return writePrev("LEFT")
        if [1, 2] in target and [2, 1] in target:
            writeMap(view, 'prevMap.dat')
            writeMap(pMap, 'prevMap2.dat')
            return writePrev("DOWN")
        if [2, 1] in target and [1, 0] in target:
            writeMap(view, 'prevMap.dat')
            writeMap(pMap, 'prevMap2.dat')
            return writePrev("RIGHT")
        if [1, 0] in target and [0, 1] in target:
            writeMap(view, 'prevMap.dat')
            writeMap(pMap, 'prevMap2.dat')
            return writePrev("UP")
    if view == ['---', '---', '--#'] and pMap == ['---', '--#', '--#']:
        writeMap(view, 'prevMap.dat')
        writeMap(pMap, 'prevMap2.dat')
        return writePrev("RIGHT")
    if view == ['#--', '#--', '#--'] and pMap == ['#--', '#--', '#--'] and pMap2 == ['#--', '#--', '#--']:
        writeMap(view, 'prevMap.dat')
        writeMap(pMap, 'prevMap2.dat')
        return writePrev("RIGHT")
    if [1, 0] in target:
        writeMap(view, 'prevMap.dat')
        writeMap(pMap, 'prevMap2.dat')
        return writePrev("UP")
    if [2, 1] in target:
        writeMap(view, 'prevMap.dat')
        writeMap(pMap, 'prevMap2.dat')
        return writePrev("RIGHT")
    if [1, 2] in target:
        writeMap(view, 'prevMap.dat')
        writeMap(pMap, 'prevMap2.dat')
        return writePrev("DOWN")
    if [0, 1] in target:
        writeMap(view, 'prevMap.dat')
        writeMap(pMap, 'prevMap2.dat')
        return writePrev("LEFT")


id = int(input())
view = []
for i in range(0, 3):
    view.append(input())

print(nextMove(view))
