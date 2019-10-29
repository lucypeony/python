import random
import time

def displayIntro():
        print('''你所在的地方有很多龙。在你前面，你看到两个洞穴。一个洞穴里，
龙很友好，会把它的财宝和你分享。另外一个洞穴里，龙贪婪而饥饿，见了就会把你吃掉...''')
        print()


def chooseCave():
        cave =''
        while cave != '1' and cave != '2':
            print('你要进入哪个洞穴？（1或者2）')
            cave = input()

        return cave


def checkCave(chosenCave):
        print('你靠近了洞穴...')
        time.sleep(2)
        print('里面又黑又吓人...')
        time.sleep(2)
        print('一个巨大的龙出现在你的面前，它张开大嘴...')
        print()
        time.sleep(2)

        friendlyCave = random.randint(1,2)

        if chosenCave == str(friendlyCave):
            print('把它的财宝给你！')
        else:
            print('一口把你吃掉！')


playAgain ='yes'
while playAgain =='yes' or playAgain =='y':
        displayIntro()
        caveNumber = chooseCave()
        checkCave(caveNumber)

        print('想重玩吗？(yes 或 no )')
        playAgain =input()


    
