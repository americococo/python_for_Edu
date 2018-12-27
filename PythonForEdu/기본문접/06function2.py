def print_round(number):
    roundnumble = round(number,1)
    print(roundnumble)
    return roundnumble

def print_sqrt(a,b,c): #매개변수#
    r1= (-b + (b**2- 4 * a * c) ** 0.5 ) / (2*a)
    r2= (-b - (b**2- 4 * a * c) ** 0.5 ) / (2*a)

    print('{}x^2 + {}x + ({})의 해는'.format(a,b,c))
    r1=print_round(r1)
    r2=print_round(r2)
    print("{} or {} 입니다 입니다".format(r1,r2))


print_sqrt(5,3,-2) # 인자

print_sqrt(29,13,0)