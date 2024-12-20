import random
while True:
    choice = input('Roll the dice?(y/n)').lower()
    if choice == 'y':
        no_dice= int(input('How many dice you want to roll?'))
        for i in range(no_dice):
            dice1 = random.randint(1,6)
            # dice2 = random.randint(1,6)

            print(f'(for dice  {i+1}->{dice1})')
        
        
    elif choice =='n':
        print('Thanks for playing1')
        break
    else:
        print('Invalid choice!')
        print("\n")