#dic = {'one':1,'two':2,'tree':3}

#dic['one'] = 11

#dic['four'] = 4 
#del (dic['one'])

#print(dic.pop('two'))
#print(dic)


ages = {'Tod':35,'jane':23,'payl':62}


for key,value in ages.items():
    print('{}의 나이는 {}입니다.'.format(key,value))


days_in_month = {"1월":31, "2월":28, "3월":31, "4월":30, "5월":31}

for key,value in days_in_month.items():
    print("{}은 {}일이 있습니다.".format(key,value) )