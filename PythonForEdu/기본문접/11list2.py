list1 = [37,23,10,33,29,40]
print(list1)
list1.append(15)
print(list1)

list2 = list1 + [16]
print(list2)

list3 = list1 + list2
print(list3)

n=12
ownership = n in list3
print(ownership)

n=10
if n in list3:
    print('{}은 잇다'.format(n))

del list3[12]

list3.remove(37)
print(list3)