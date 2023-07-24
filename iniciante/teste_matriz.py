for x in range(1, 12):
    for y in range(11, 0, -1):
        print('%d * %d = %d' % (x, y, x*y))
        if (x == y):
            print