
class RevStr(str):
    def __str__(self):
        return self[::-1]

def main():
    hello = RevStr('Hello World !')
    newhello = RevStr(hello)
    print('-------------------------------------')
    print('| ', hello, ' => ', newhello, ' |' )
    print('-------------------------------------')
if __name__ == "__main__":main()