import heroes

# intro to the game
print('Hello and welcome to Guess that Hero!\nDo you want to play y/n: ')
play = input().lower()


if play == 'y':
    print('Lets gooooo!')
elif play == 'n':
    print('Sorry to hear that </3 maybe next time..')
    input('Press a key to exit')
    exit()
else:
    print('You had 1 job and you fucked it up. Good job....')
    input('Press a key to exit')
    exit()


# lives of the player
lives = 3
# index of the character
x = 0

# start game
while lives > 0 and x < len(heroes.heroes):
    print('--------------------------')
    print('Lives: ', lives)
    print('\nWho is this hero?\n', heroes.heroes.get(x))
    guess = input()

    if guess == heroes.heroes.get(x):
        print('That is correct!')
        x += 1
    else:
        print('That isn\'t right! Try again')
        lives -= 1

# game ending
if lives > 0:
    print('Congrats, you made it to the end! You are a true gamer ♥')
    print('You only answered ', 3 - lives, ' questions wrong! Well done')
else:
    print('You almost made it. Read up on your overwatch lore and try again.\nMaybe you will get it next time ♥')
