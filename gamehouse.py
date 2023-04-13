import random
users ={'ultraboy':{'password':'1234', 'email': 'ultraboy@gmail.com', 'fullname':{'first_name': 'Denzel', 'last_name': 'Ojo'}},
        'superboy':{'password':'5432', 'email': 'superboy@gmail.com', 'fullname':{'first_name': 'Victor', 'last_name': 'Adebote'}},
        'okelagirl':{'password':'5454', 'email': 'okelagirl@gmail.com', 'fullname':{'first_name': 'Olivia', 'last_name': 'Ojo'}}
        }

username=input('Username: ')
password=input('password: ')
if username in users and password==users[username]['password']:
        print('logged in successfully\n')
        print(f'''these are your details:
        first name= {users[username]['fullname']['first_name']}
        last name= {users[username]['fullname']['last_name']}
        email= {users[username]['email']}\n''')
        users_choice = input('what game do you want to play:number guessing game or rock paper scissors\n').lower()
        if users_choice=='number guessing game':
           print('''
           ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░  ████████╗██╗░░██╗███████╗
           ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗  ╚══██╔══╝██║░░██║██╔════╝
           ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║  ░░░██║░░░███████║█████╗░░
           ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║  ░░░██║░░░██╔══██║██╔══╝░░
           ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝  ░░░██║░░░██║░░██║███████╗
           ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝

           ░██████╗░██╗░░░██╗███████╗░██████╗░██████╗██╗███╗░░██╗░██████╗░  ░██████╗░░█████╗░███╗░░░███╗███████╗
           ██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝██║████╗░██║██╔════╝░  ██╔════╝░██╔══██╗████╗░████║██╔════╝
           ██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░██║██╔██╗██║██║░░██╗░  ██║░░██╗░███████║██╔████╔██║█████╗░░
           ██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗██║██║╚████║██║░░╚██╗  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
           ╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝██║██║░╚███║╚██████╔╝  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
           ░╚═════╝░░╚═════╝░╚══════╝╚═════╝░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝

                                                     ░█████╗░
                                                      ██╔══██╗
                                                      ╚═╝███╔╝
                                                      ░░░╚══╝░
                                                      ░░░██╗░░
                                                      ░░░╚═╝░░''')
           computers_choice = random.randint(0,10)
           print('The computer has just chosen a number between 0 and 9 can you guess it?\n')
           num_of_lives=3
           while num_of_lives != 0:
                   print(f'{num_of_lives} attempts left\n')
                   users_choice = int(input('guess the number '))
                   if users_choice==computers_choice:
                       print('the user has won!')
                       break
                   elif users_choice > computers_choice:
                        print('the user\'s choice is too high\n')
                   else:
                       print ('the users choice is too low\n')
                   num_of_lives  -= 1
        elif users_choice=='rock paper scissors':
            rock = '''    
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)'''
            paper = '''    
                _______
            ---'   ____)____
                      ______)
                      _______)
                     _______)
            ---.__________)
            '''
            scissors = '''   
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)'''
            user_action = input("Enter a choice (rock, paper, scissors): ").lower()
            possible_actions = ["rock", "paper", "scissors"]
            computer_action = random.choice(possible_actions)
            hand_actions = {'rock': rock, 'paper': paper, 'scissors': scissors}
            print(
                f"\nYou chose {hand_actions.get(user_action)}, \ncomputer chose {hand_actions.get(computer_action)}.\n")

            if user_action == computer_action:
                print(f"Both players selected {user_action}. It's a tie!")
            elif user_action == "rock":

                if computer_action == "scissors":
                    print("Rock smashes scissors! You win!")
                else:
                    print("Paper covers rock! You lose.")
            elif user_action == "paper":
                if computer_action == "rock":
                    print("Paper covers rock! You win!")
                else:
                    print("Scissors cuts paper! You lose.")
            elif user_action == "scissors":
                if computer_action == "paper":
                    print("Scissors cuts paper! You win!")
                else:
                    print("Rock smashes scissors! You lose.")
else:
    print('incorrect login details')
