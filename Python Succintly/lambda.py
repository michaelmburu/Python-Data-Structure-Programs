# Lambda functions in python

# Normal function call
def edit_story(words, func):
    for word in words:
        print(func(word))

def enliven(word):
    return word.capitalize() + '!'

song  = ['Woof', 'Meouw', 'Bark']

print('Without lambda. \n')

edit_story(song, enliven)
print('\n')

#Simple lanbda call
print('After Lambda. \n')
edit_story(song, lambda word: word.capitalize() + '!')
    