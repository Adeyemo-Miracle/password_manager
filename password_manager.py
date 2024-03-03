pwd = input('What is the master password?')
def view():
    with open('passwords.txt', 'r') as f:
        for x in f.readlines():
            data = x.rstrip()
            user, passw = data.split('|')
def add():
    name= input('Account Name: ')
    pwd = input('Password: ')
    
    with open('passwords.txt', 'a') as f:
        f.write(name + '|' + pwd + '\n')

while True:
    mode = input('would you like add a new password or view existing ones (view/add), press "q" to quit ')
    if mode == 'q':
        break
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid mode. ')
        continue


