

def main():
    infile = open('dummyfile.txt', 'rt')
    outfile = open('newfile.txt', 'wt')
    print('\n------------------------------------------------------------------------------------')
    print('\t \t \t New File creation Started')
    print('------------------------------------------------------------------------------------')
    for line in infile:
        print(line.rstrip(), file=outfile)
        print('*', end = '   ', flush=True)
    outfile.close()
    infile.close()
    print('\n------------------------------------------------------------------------------------')
    print('\t \t \t  New File Creation job is completed')
    print('------------------------------------------------------------------------------------')

if __name__ == "__main__":main()