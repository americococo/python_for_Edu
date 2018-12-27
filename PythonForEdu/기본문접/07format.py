
number = 20
greeting = '안녕하세요'
place = '문자열 포맷의 세계'
welcome = '환영합니다'


print(number,'번 손님',greeting,'.\n',place,'에 오신 것을 ',welcome,'!!')

base = '{}번 손님,{}, .\n {}에 오신 것을 {}!!'
new_way = base.format(number,greeting,place,welcome)
#format-> 인자로 받은 같을 문자열에 {}와 순서대로 교체

print(base)
print(new_way)