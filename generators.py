

def main():
   for i in inclusive_range(15):
       print (i, end = '   ')


def inclusive_range(*args):
    numbers = len(args)
    print('Numbers of arguments passed {}'.format(numbers))
    start = 0
    step = 1

    # Initialize parameters
    if numbers < 1:
        raise TypeError(f'Expected atleast one aragement, you have passed {numbers} argument')
    elif numbers == 1:
        stop == args
        print('New Stop value is = {}'.format(stop))
        
    elif numbers == 2: 
        (start, stop) = args
    elif numbers == 3:
        (start, stop, step) = args
    else: raise TypeError(f'Maximum 3 arguments are allowed, You have passed {numbers} arguments ')

   
    # Generators
    i = start
    while i <= stop:
        yield i
        i += step    


if __name__ == "__main__": main()
    