import random
while True:
    choice = input('Roll the dice?(y/n)').lower()
    if choice == 'y':
        dice1 = random.randint(1,6)
        # dice2 = random.randint(1,6)
        print(f'({dice1})')
    elif choice =='n':
        print('Thanks for playing1')
        break
    else:
        print('Invalid choice!')
        print("\n")