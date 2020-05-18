

def main():
    animals = dict(kitten = 'Meow', puppy = 'Lol Lol', lion = 'Irr Iree', monkey = 'ha ha ha')
    print_dict(animals)

def print_dict(o_dic):
    for k, v in o_dic.items():
        print(k, ' -----> ', v , end = '   ', flush= True)
        print()


if __name__ == "__main__":main()
    