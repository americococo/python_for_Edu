import random
r_s_p = ['rock','scissor','papper'] #array

wintable = {r_s_p[0]:r_s_p[1], r_s_p[1]:r_s_p[2],r_s_p[2]:r_s_p[0]} 
#"""dictory 키값:실제 값

def rsp(mine_choice,cp_choice):
    if mine_choice == cp_choice:
        return 'draw'
    elif wintable[mine_choice] == cp_choice:
        return 'win'
    else:
      return 'lose'

me = input('rock scissor papper ?')
cpu =  random.choice(r_s_p)


result = rsp(me,cpu)

print(result)