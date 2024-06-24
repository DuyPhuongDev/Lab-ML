def dinamod():
    n = int(input("enter high of dinamod: "))
    for i in range(n):
        if(i==n//2): print('*'*n)
        elif(i<n//2):
            print(' '*(n//2-i) + '*' * ((i+1)*2-1))
        else:
            print(' '*(i-n//2)+ '*'*((n-i)*2-1))
            



import numpy as np

def mulGame():
    for i in range(10):
        a = np.random.randint(0,10)
        b = np.random.randint(0,10)
        ques = f"Question {i+1}: {a} x {b} = "
        ans = int(input(ques))
        if(ans == a*b):
            print('Right!')
        else:
            print(f'Wrong. The answer is {a*b}.')


def loopEx():
    passWord = input('Create new password: ')
    count = 5
    while True:
        if(count==0):
            print('They are kicked off the system!')
            break
        ans = input('Enter password: ')
        if(ans==passWord):
            print('They are logged into the system!')
            break
        count-=1
        print(f'Password incorrect. You have {count} to try.')

loopEx()