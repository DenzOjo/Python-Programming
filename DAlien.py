'''
Imagine an alien was just shot down in a game.
Alien
Create a variable called alien_color that collects an input from the user a value of either  'green', 'yellow', or 'red'.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points
'''
#Alien
alien_colour=input('pick a colour:red,green,yellow,blue,orange\n')#makes you put in an input with options and will name your input called alien_clour

if alien_colour=='red':#uses if statement to create a loop through your input with different answers depending on your input
        print('Congratulations, You have earned 15 points!')
elif alien_colour=='yellow':
        print('Bravo, You have earned 10 points!')
elif alien_colour=='green':
        print('nice, you have earned 5 points')
else:
        print('sorry that is not the aliens colour try again')


