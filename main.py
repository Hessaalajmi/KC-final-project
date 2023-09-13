print('Hello and welcome to What\'s on, Here we will help you to choose your summer activity.')
name = input('Enter your name: ')
age = int(input('Enter your age: '))
prefer = input('  1-coding \n  2-STEM \n  3-cinema \n  4-robotics  \n Please choose a number from ubove: ')
                     


if  age >= 14 and age < 18:
    if prefer == '1':
        print(f'Hi {name}, You should join Kuwait codes they have great coding classes.')
    elif prefer == '2':
        print(f'Hi {name}, You should join CSO seniors they will give you interesting STEM lectures.')
    elif prefer == '3':
        print(f'Hi {name}, You should join lapa teens cinema program they will give you interesting cinema lessons.')
    elif prefer == '4':
        print(f'Hi {name}, You should join Makers camp YPA or Youth creativity league (robotics) they have great robotics lessons')
    else:
        print('Please choose a valid number from the list.')
elif age >= 8 and age <= 13:
    if prefer == '1':
        print(f'Hi {name}, You should join Coded Juniors they have great coding classes.')
    elif prefer == '2':
        print(f'Hi {name}, You should join CSO juniors they will give you interesting STEM lectures.')
    elif prefer == '3':
        print(f'Hi {name}, You should join lapa kids cinema program they will give you interesting cinema lessons.')
    elif prefer == '4':
        print(f'Hi {name}, You should join Makers camp YPA or Youth creativity league (robotics) they have great robotics lessons')
    else:
        print('Please choose a valid number from the list.')
elif age >= 18:
    if prefer == '1':
        print(f'Hi {name}, You should join Uni codes they have great coding classes.')
    elif prefer == '2':
        print(f'Hi {name}, You should Join KFAS\'s STEM related programs.')
    elif prefer == '3':
        print(f'Hi {name}, You should join lapa program\'s they will give you interesting cinema lessons.')
    elif prefer == '4':
        print(f'Hi {name}, You should join EBOT YPA they have great robotics lessons')
    else:
        print('Please choose a valid number from the list.')
else:
    print('There are no programs for your age or The age you entered is no valid.')
