'''
Hello Admin: Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user:
• If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for
logging in again.
'''
username=['joseph','preston','david','christy','admin']#list of users
for user in username:#uses loop to check through the list if admin (special statement ,if not normal statement)
    if user=='admin':
        print('Hello Admin would you like a status report on all users')
    else:
        print(f'Hello there thank you for logging in {user}')