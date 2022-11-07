import lib

pseudo = input('\t- Je suis Python. Quel est votre pseudo ? \n ')

print(f'\t- Hello {pseudo}, vous avez 10 €, Très bien ! Installez vous SVP à la table de pari.\n\t\t\t Je vous expliquerai le principe du jeu : \n')
print('\t- Att : vous avez le droit à trois essais !\n')
print('\t- Si vous devinez mon nombre dès le premier coup, vous gagnez le double de votre mise !\n')
print('\t- Si vous le devinez au 2è coup, vous gagnez exactement votre mise !\n')
print('\t- Si vous le devinez au 3è coup, vous gagnez la moitiè votre mise !\n ')
print('\t- Si vous ne le devinez pas au 3è coup, vous perdez votre mise et')
print('\tvous avez le droit : ')
print('\t\t- de retenter votre chance avec l\'argent qu\'il vous reste pour reconquérir le level perdu.')
print('\t\t- de quitter le jeu.\n')
print('\t- Dès que vous devinez mon nombre : vous avez le droit de quitter le jeu et de partir avec vos gains OU \n\t\tde continuer le jeu en passant au level supérieur.\n  ')


def game(level, attempts, start, stop):
    betted = lib.getBetting()
    toGuess = lib.chooseNumber(start, stop)
    print(toGuess)
    print(
        f'\t- Je viens de penser à un nombre entre 1 et {10*level}. Devinez lequel ?\n')
    guessed = lib.getGuessing(attempts, level)
    guess = lib.validateGuessing(toGuess, guessed)
    print(guess)

    attempts = 1
    while attempts < 3 and guess != True:
        guessed = lib.getGuessing(3-attempts, level)
        guess = lib.validateGuessing(toGuess, guessed)
        print(guess)
        attempts += 1

    # TODO: calculate the gain properly
    gain = lib.calculateGain(attempts, guess, betted)

    if guess == True:
        print(
            f'\t- Bingo {pseudo}, vous avez gagné en {attempts} coup(s) et vous avez remporté {gain} € !\n')
        nextStep = lib.pursue()
        if (nextStep == 'O'):
            level += 1
            print(f'\t- Super ! Vous passez au Level {level}.\n')
            print(
                f'\t- Rappelez vous, le principe est le même sauf que mon nombre est maintenant entre 1 et {level*10} et\n\t\t vous avez le droit à {3+level*2} essais !\n')
            game(level, 3, 1, level*10)
        elif nextStep == 'N':
            print(f'\t- Au revoir ! Vous finissez la partie avec {gain} €.\n ')
    else:
        print(
            f'\t- Vous avez perdu ! Mon nombre était {toGuess} ! Il vous reste {10-betted} €\n')
        nextStep = lib.pursue()
        if nextStep == 'O':
            level = 1
            print(f'\t- Super ! Vous repassez au Level {level}.\n')
            print(
                f'\t- Rappelez vous, le principe est le même sauf que mon nombre est de nouveau entre 1 et {level*10} et\n\t\t vous avez le droit à 3 essais !\n')
            game(level, 3, 1, level*10)
        elif nextStep == 'N':
            print(f'\t- Au revoir ! Vous finissez la partie avec {gain} €.\n ')

game(1, 3, 1, 10)
