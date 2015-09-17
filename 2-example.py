#!/usr/bin/env python
# 2-example
# A simple demonstration script to find the largest prime number
# below a given limit.
#
# This file is intentionally inefficient in order to demonstrate
# various ways to time execution
#
# Usage:
#   python 2-example.py 10000
#
# Author:   Allen Leis <al1075@georgetown.edu>
# Created:  Wed Sep 13 21:50:05 2015 -0400
#
# Copyright (C) 2015 georgetown.edu
# For license information, see LICENSE.txt
#
# ID: 2-example.py [] al1075@georgetown.edu $

"""
A simple demonstration script to find the largest prime number
below a given limit.
"""

##########################################################################
## Imports
##########################################################################

import sys
import time

##########################################################################
## Code
##########################################################################

def is_prime(limit):
    """
    Using the most time intensive method possible, return True or False
    as to whether the supplied number is prime
    """
    for number in range(2,limit):
        if (limit % number) == 0:
            return False
    return True


def find_largest_prime(limit):
    """
    Find the highest number below the supplied limit/upper bound
    that is a prime number
    """
    i = 2
    largest_prime = None

    while i < limit:
        if is_prime(i):
            largest_prime = i
        i += 1
    return largest_prime


##########################################################################
## Execution
##########################################################################

if __name__ == '__main__':
    upper_bound = int(sys.argv[1])
    start = time.time()
    print find_largest_prime(upper_bound)
    elapsed = time.time() - start
    print 'elapsed time: %0.2fs' % elapsed


