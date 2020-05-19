

def main():
    f = open('list.py', 'r')
    for line in f:
        print(line.rstrip())

if __name__ == "__main__":main()