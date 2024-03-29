
# Gra logiczna polegająca na odgadnięciu trzycyfrowej liczby #

import random

NUM_DIGITS = 3
MAX_GUESSES = 100

def main():
    print('''Zgadnij jaka to liczba?
Odgadnij {}-cyfrową liczbę, korzystając z następujących podpowiedzi:
Gdy pojawi się:
Maron - Jedna cyfra jest poprawna, ale jest na złej pozycji
Hasan - Jedna cyfra jest poprawna i jest na odpowiedniej pozycji
Memlo - Żadna cyfra nie jest poprawna'''.format(NUM_DIGITS))
    
    while True:
        secretNum = getSecretNum()
        print('Mam na mysli liczbę')
        print(' Masz {} prób, aby odgadnąć ukrytą liczbę'.format(MAX_GUESSES))
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ' '
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Próba #{} : '.format(numGuesses))
                guess = input('>')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('Wykorzytsałeś wszystkie próby')
                print('Prawidłowa cyfra to {}.'.format(secretNum))      
        print("Czy chcesz zagrać ponownie? (tak lub nie)")
        if not input('>').lower().startswith('t'):
            break
    print('Dziękuje za grę')

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum
    
def getClues(guess, secretNum):
    if guess == secretNum:
        return 'Zgadłeś!'
    
    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Hasan')
        elif guess[i] in secretNum:
            clues.append('Maron')
    if len(clues) == 0:
        return 'Memlo'
    else:
        clues.sort()
        return ' '.join(clues)
    
if __name__ == '__main__':
    main() 
            
      
    
        
        

