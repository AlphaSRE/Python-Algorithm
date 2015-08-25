#coding=utf-8
#有两个序列a,b，大小都为n,序列元素的值任意整形数，无序；
#要求：通过交换a,b中的元素，使[序列a元素的和]与[序列b元素的和]之间的差最小
import random
#listA = [random.randint(0,100) for i in range(10)]
#listB = [random.randint(0,100) for i in range(10)]
listA = [100,2,3,4]
listB = [500,6,7,8]

Source = listA + listB
lista = []
listb = []

Source.sort()

max = Source[-1]
second = Source[-2]

lista.append(max)
listb.append(second)
for i in Source[-3::-1]:
    if sum(lista) > sum(listb) and len(listb) < len(listA):
        listb.append(i)
    else:
        lista.append(i)

print lista,listb
print abs(sum(lista)-sum(listb))
