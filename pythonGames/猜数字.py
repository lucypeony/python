#这是一个猜数字游戏
import random

gussesTaken=0
print('请输入你的名字')
myName=input()


number = random.randint(1,20)
print("你好， "+ myName + ',这个数字在1到20之间。')

for guessesTaken in range(6):
    print('猜一下。')
    guess = input()
    guess = int(guess)

    if guess <number:
        print('你猜的数字太小了。')

    if guess > number :
        print('你猜的数字太大了。')

    if guess == number :
        break

if guess == number:
    guessesTaken = str(guessesTaken+1)
    print('不错，' + myName + '!，你用了'+ guessesTaken + '次猜对了数字！')

if guess != number:
    number = str(number)
    print('猜错了。我想的数字是'+ number)
    
