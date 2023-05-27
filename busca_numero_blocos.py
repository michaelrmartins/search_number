#!/usr/bin/python
#-*- encoding: utf-8 -*-
'''
# Create and Search by a number using block Search patern.
# Michael MArtins - 2023
'''
# Libraries
import os
import time
from timeit import default_timer as timer
import subprocess
import random

# Variables
golden_number = 0
sequential_number = 0000
sampling = 1000

loop = 1

while loop < sampling :
    # Generate pseudo-random number
    golden_number = random.randrange(0,9999)
    loop += 1
    start = timer()

    # Step one
    for x in range (1,999):
        if (x == golden_number):
            sequential_number = x
            break

    # Step two
    for x in range (5000,5999):
        if (x == golden_number):
            sequential_number = x
            break

    # Step three
    for x in range (1000,1999):
        if (x == golden_number):
            sequential_number = x
            break

    # Step four
    for x in range (6000,6999):
        if (x == golden_number):
            sequential_number = x
            break

    # Step five
    for x in range (2000,2999):
        if (x == golden_number):
            sequential_number = x
            break

    # Step six
    for x in range (7000,7999):
        if (x == golden_number):
            sequential_number = x
            break

    # Step seven
    for x in range (3000,3999):
        if (x == golden_number):
            sequential_number = x
            break

    # Step eight
    for x in range (8000,8999):
        if (x == golden_number):
            sequential_number = x
            break

    # Step nine
    for x in range (4000,4999):
        if (x == golden_number):
            sequential_number = x
            break

    # Step ten
    for x in range (9000,9999):
        if (x == golden_number):
            sequential_number = x
            break

    end = timer()

    # print CSV
    print (str(sequential_number)+ ";" + str(end - start))
    
    # print (sequential_number)
    #print (end - start)