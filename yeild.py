

def main():
   for i in inclusive_range(100000):
       print (i, end = '   ')


def inclusive_range(n):
    # Generators
    i = 0
    while i <= n:
        yield i
        i += 10000   


if __name__ == "__main__": main()
    