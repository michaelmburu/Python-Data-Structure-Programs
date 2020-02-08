messages = [['0721333444', 'Change your password now'], ['07213543555', 'Paypal confirmation code'], ['07098888888','Dear equity member change your pin now']]
a = 0
# Using while loop
print('Using while loop')

while a < len(messages):
    print(messages[a])
    print('\n')
    a += 1

# Using for loop
print('\n')
print('\n')
print('Using for loop')
for message in messages:
    print(message[0])
print('\n')


