import random

NUM_DIGITS = 3
MAX_GUESS = 10

def getSecretNum():
    #Returns a string of unique random digits that is NUM_DIGITS long.
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum=''
    for i in range(NUM_DIGITS):
        secretNum +=str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    #Returns a string with Pico, Fermi, &Bagels clues to the user.
    if guess == secretNum:
        return 'You got it!'

    clues =[]
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')

    if len(clues) ==0:
        return 'Bagels'

    clues.sort()
    return ''.join(clues)

def isOnlyDigits(num):
    if num =='':
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9 '.split():
            return False
    return True
    


print('我在想一个 %s 位的数字， 你猜猜它是什么。'%(NUM_DIGITS))
print('我给的线索是......')
print('我说的话：     我的话的含义:')
print(' Bagels         没有一个数字是正确。')
print(' Pico           一个数字是正确的，但位置是错误的')
print(' Fermi          一个数字是正确的，位置也是正确的')

while True:
    secretNum = getSecretNum()
    print('I have thought up a number. You have %s guesses to get it.' %(MAX_GUESS))

    guessesTaken =1
    while guessesTaken <= MAX_GUESS:
        guess =''
        while len(guess) != NUM_DIGITS or not isOnlyDigits(guess):
            print('Guess #%s: '%(guessesTaken))
            guess = input()

        print(getClues(guess,secretNum))
        guessesTaken +=1

        if guess == secretNum:
            break
        if guessesTaken > MAX_GUESS:
            print('You ran out of guesses. The answer was %s.' %(secretNum))

    print('do you want to play again?(yes or no)')
    if not input().lower().startswith('y'):
        break
    
