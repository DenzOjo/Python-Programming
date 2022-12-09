''''
3-6. More Guests: You just found
3-7. Shrinking Guest List: You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
• Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
• Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
• Print a message to each of the two people still on your list, letting them9
know they’re still invited.
• Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.
'''
print()
guest_list=['Denzel', 'Olivia', 'Andrea', 'Alex', 'Femi', 'Tunde']
print('We are sorry to inform everyone that only two people will be invited to dinner sorry for\n any inconvinience')
guest_list.pop(0)
print('we are sorry Denzel you cant join dinner')
guest_list.pop(1)
print('we are sorry Olivia you cant join dinner')
guest_list.pop(2)
print('we are sorry Andrea you cant join dinner')
guest_list.pop(-3)
print('we are sorry Femi you cant join dinner')
print(guest_list)
print('congratulations Alex you are still invited to dinner')
print('congratulations Tunde you are still invited to dinner')
del guest_list [-2]
del guest_list [-1]
print(guest_list)