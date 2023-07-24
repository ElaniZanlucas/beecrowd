# PUM
# Repetição

# -*- coding: utf-8 -*-

n = int(input())
count3 = -1

for item in range(n):
    count1 = count3 + 2
    count2 = count1 + 1
    count3 = count2 + 1
    print("{} {} {} PUM" .format(count1, count2, count3))