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

betted = lib.getBetting()
toGuess = lib.chooseNumber(1, 10)
guessed = lib.getGuessing()
correct = lib.validateGuessing(toGuess, guessed)

print(correct)
