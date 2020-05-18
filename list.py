#!/usr/bin/env python3
#This is for List datatype
# List is mutable object which means can modigy any value in the list and also can add or delete the elements in the list

def main():
    game = ['Cricket', 'Foodball', 'Hockey', 'Kapadi', 'Gilli', 'Dayam', 'Goli']
    print_list(game)

    game [2] = 'Running'
    print_modified_list(game)

    game.append('Snookar')
    print_new_list(game, 'Added')

    game.remove('Dayam')
    print_new_list(game, 'Deleted')

def print_list(olist):
    for i in olist:
        print(i, end = '   ', flush=True)
        print()
    print('------------------------------------')


def print_modified_list(olist):
    print('Modified List')
    for i in olist:
        print(i, end = '   ', flush=True)
        print()
    print('------------------------------------')


def print_new_list(olist, st_action):
    print('An item {} for list '.format(st_action))
    for i in olist:
        print(i, end = '   ', flush=True)
        print()
    print('------------------------------------')

if __name__ == "__main__":main()
    