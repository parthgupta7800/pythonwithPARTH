import random as r
val=r.random()
print('Hey! Welcome to the best OTP generator')
print('Enter which type of OTP you want\n1. 4 digit\n2. 6 digit\n3. alpha numeric')
n=int(input())
if n==1:
    otp=str(val)[-4:]
    print(otp)
elif n==2:
    otp=str(val)[-6:]
    print(otp)
elif n==3:
    str='123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    val2=''.join(r.choices(str,k=6))
    print(val2)
