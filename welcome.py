#!/usr/bin/env python3
#Copyright 2020 Tharanibabu

import platform

print('Welcome !')

# functions defanision

def getPlatformVersion():
    print('This is Python Version {}'.format(platform.python_version()))

def getOtherDetails():
    print('Python compiler is {}'.format(platform.python_compiler()))
    print('Python implementation is {}'.format(platform.python_implementation()))
    print('Python revision is {}'.format(platform.python_revision()))   

# Main functions 
if __name__ == "__main__":
    getPlatformVersion()
    getOtherDetails()