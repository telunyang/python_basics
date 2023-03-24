# 9 x 9 乘法表
for i in range(1, 10):
    for j in range(1, 10):
        print('%d x %d = %d' % (i, j, i * j), end="\t")
    print()