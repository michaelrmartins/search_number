#!/usr/bin/python
#-*- encoding: utf-8 -*-
'''
# Create and Search by a number using sequencial Search patern.
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
while loop < sampling:
    # Generate pseudo-random number
    golden_number = random.randrange(0,9999)
    loop += 1
    start = timer()
    
    # Search
    for x in range (1,9999):
        if (x == golden_number):
            sequential_number = x
            break

    end = timer()

    # print CSV
    print (str(sequential_number)+ ";" + str(end - start))

    #print (sequential_number)
    #print (end - start)