import random
s=5
n=random.randint(1,100)
print('Enter the your name')
name=input()
print(f'Hey ! {name}, Welcome to the game zone of guess the number ')

for i in range (5):
    print('Enter the number ')
    un=int(input())
    if n==un:
        print('WOW!! you Won this game')
        break
    else:
        if n>un:
            print('Ooops!!, try something greater')
        else:
            print('Ooops!!, try something smaller')
        s-=1
        if s>0:
            continue
        else:
            print('Sorry you lose')
    
