def snail(table):
    dimension = len(table)
    matrix = table[0]

    start = dimension + 1
    end = int(dimension ** 2)
    index = 0

    # print(start)
    # print(end)

    # create borders
    x, y = 0, dimension - 1

    # fulfill lines in four directions
    while start <= end:
        # to the down
        for i in range(x + 1, y + 1):
            if start > end:
                break
            else:
                matrix.append(table[i][y])
                start += 1

        # to the left
        for i in range(y - 1, x - 1, -1):
            if start > end:
                break
            else:
                matrix.append(table[y][i])
                start += 1

        # to the up
        for i in range(y - 1, x, -1):
            if start > end:
                break
            else:
                matrix.append(table[i][x])
                start += 1

        # to the right
        for i in range(x + 1, y):
            if start > end:
                break
            else:
                matrix.append(table[x + 1][i])
                start += 1

        x += 1
        y -= 1

    # output answer in correct form
    return matrix
