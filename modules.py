
import os
def main():
    v = os.urandom(25)
   
    print(v.hex())
 

if __name__ == "__main__":main()