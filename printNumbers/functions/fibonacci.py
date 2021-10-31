# -*- coding: utf-8 -*-
#
# fibonacci.py
#
# This file is part of printNumbers.
#
# Copyright (C) 2017 G. Trensch, SLNS, JSC, FZ Jülich
#
# printNumbers is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# printNumbers is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with printNumbers.  If not, see <http://www.gnu.org/licenses/>.

def FibonacciRecursion(n):
    '''
    Helper function.
    '''
    if n <= 1:
        return n
    else:
        return (FibonacciRecursion(n - 1) + FibonacciRecursion(n - 2))

def FibonacciSequence(n):
    '''
    :param n:   Operand
    :return:    fib(n) as list of fibonacci numbers, [0, 1, 1, 2, ... ]
    '''
    # sequence = []
    # for i in range(n):
    #     sequence.append(FibonacciRecursion(i))
    # return (sequence)
    
    # Zhang's version
    fib = [0]*n
    if n>0: fib[0] = 0
    if n>1: fib[1] = 1
    for i in range(2,n):
        fib[i] = fib[i-1] + fib[i-2]
    return fib
