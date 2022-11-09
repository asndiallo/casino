import random


def getBetting():
    try:
        betting = int(input('\t- Le jeu commence, entrez votre mise : ?\n'))

        while betting not in range(1, 11):
            betting = int(input(
                '\t- Le montant saisi n\'est pas valide. Entrer SVP un montant entre 1 et 10 € :  ?\n '))
        return betting
    except ValueError:
        print('\nCe n\'était pas un nombre valide. Veillez recommencer \n')
        getBetting()


def chooseNumber(start, stop):
    return random.randint(start, stop)


def calculateGain(attempts, guess, betted):
    if isinstance(attempts, int) and isinstance(betted, int):
        if attempts == 3 and guess == True:
            gain = betted/2
        elif attempts == 2 and guess == True:
            gain = betted
        elif attempts == 1 and guess == True:
            gain = 2*betted
        else:
            gain = 0
        return gain


def getTotalBalance(gain, betted):
    return 10-betted+gain


def getGuessing(remainingAttempts, level):
    try:
        guessing = int(input(
            f'\t- Alors quel nombre ai-je choisie : ?\n\t Il vous reste {remainingAttempts} essai(s) !\n'))
        if guessing not in range(1, (10*level + 1)):
            guessing = int(
                input(f'\t- Je ne comprends pas ! Entrer SVP un nombre entre 1 et {10*level} :  ?\n'))
            getGuessing(remainingAttempts, level)
        return guessing
    except ValueError:
        print(
            (f'\t- Je ne comprends pas ! Entrer SVP un nombre entre 1 et {10*level} :  ?\n'))
        getGuessing(remainingAttempts, level)


def validateGuessing(toGuess, guessed):
    if isinstance(toGuess, int) and isinstance(guessed, int):
        if guessed > toGuess:
            return '\t- Votre nombre est trop grand !\n'
        elif guessed < toGuess:
            return '\t- Votre nbre est trop petit !\n'
        else:
            return guessed == toGuess


def pursue():
    nextStep = input(
        '\t- Souhaitez-vous continuer la partie (O/N) ?\n').upper()
    while nextStep != 'O' and nextStep != 'N':
        print('\t- Je ne comprends pas votre réponse.')
        nextStep = pursue()
    return nextStep


def pursuing(level, maxAttempts):
    print(f'\t- Super ! Vous passez au Level {level}.\n')
    print(
        f'\t- Rappelez vous, le principe est le même sauf que mon nombre est maintenant entre 1 et {level*10} et\n\t\t vous avez le droit à {maxAttempts} essais !\n')
