def print_sqrt():
    r1= (-b + (b**2- 4 * a * c) ** 0.5 ) / (2*a)
    r2= (-b - (b**2- 4 * a * c) ** 0.5 ) / (2*a)

    print('{}x^2 + {}x + ({})의 해는'.format(a,b,c))
    print("{} or {} 입니다 입니다".format(r1,r2))

a=1
b=2
c=-8
print_sqrt()



a=2
b=-6
c=-8

print_sqrt()