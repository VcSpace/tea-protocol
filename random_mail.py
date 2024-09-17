import random
import string

in_pwd = 'ksdsdd*1212aa88'
def generate_random_email():
    prefix_length = random.randint(7, 11)
    prefix = ''.join(random.choice(string.ascii_lowercase) for _ in range(prefix_length))

    email = prefix + "@kravify.com"
    print(email,'###\n')
    with open("reg.txt", 'a') as f:
        f.write(str(email) + "----")

    return email


def generate_random_name():
    prefix_length = random.randint(7, 11)
    prefix = ''.join(random.choice(string.ascii_lowercase) for _ in range(prefix_length))

    name = prefix + "23"
    with open("reg.txt", 'a') as f:
        f.write(str(name) + '----' + in_pwd + '----')
    print(name,'\n')

    return name

def input_pv():
    pvp = input("enter pv \n : ")
    with open("reg.txt", 'a') as f:
        f.write(str(pvp) + '\n')

if __name__ == '__main__': #

    print('user_name:   ')
    generate_random_name()
    print('user_mail:    ')
    generate_random_email()
    print(in_pwd, '\n')
    input_pv()