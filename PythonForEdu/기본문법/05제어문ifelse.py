import random

scissor = 'scissor'
rock = 'rock'
papper = 'papper'

rockscissorpapper=[rock,scissor,papper]

win= '이김'
draw = '비김'
lose = '짐'

mine = scissor
you = rock


print('가위: 1 \t 바위:2 \t 보:3')
mine = input()

if mine == '1':
    mine = scissor
if mine == '2':
    mine = rock
else:
    mine = papper


you = rockscissorpapper[random.randrange(0,3)]

if mine == you:
    result = draw

else:
    if mine == scissor:
        if you == rock:
            result = lose
        else:
            result = win
    elif mine == rock:
        if you == papper:
            result = lose
        else:
            result = win
    elif mine == papper:
        if you == scissor:
            result = lose
        else:
            result = win

print('\n\n내가 선택한것 {0} \n\ncp가 선택한것 {1}\n\n'.format(mine,you))
print('{0}'.format(result))