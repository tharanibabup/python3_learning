
def main():
    infile = open('longon.jpeg', 'rb')
    outfile = open('newLondon.jpeg', 'wb')
    print('\n------------------------------------------------------------------------------------')
    print('\t \t \t New Image File creation Started')
    print('------------------------------------------------------------------------------------')
    while True:
        buf = infile.read(10240)
        if buf:
            outfile.write(buf)
            print('*', end = '   ', flush=True)
        else: break
    outfile.close()
    infile.close()
    print('\n------------------------------------------------------------------------------------')
    print('\t \t \t  New Image File Creation job is completed')
    print('------------------------------------------------------------------------------------')

if __name__ == "__main__":main()