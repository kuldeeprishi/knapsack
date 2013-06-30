# ####################################################
#
# Solution to Knapsack Problem
# Using Lookup Table
#
# ####################################################




#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def kptable(items, k):
    # create empty table with len(items)+1 columns and k+1 rows
    table = [[0 for cols in xrange(len(items)+1)] for rows in xrange(k+1)]
    for i in xrange(1, k+1):
        for j in xrange(1, len(items)+1):
            val, wt = items[j-1]
            if wt > i:
                table[i][j] = table[i][j-1]
            else:
                table[i][j] = max(table[i][j-1], val + table[i -wt][j-1])
    # traceback which item to be taken
    result = 0
    taken = [0 for i in range(len(items))]
    i = k
    for j in xrange(len(items), 0, -1):
        was_added = table[i][j] != table[i][j-1]
        if was_added:
            if result == 0:
                result = table[i][j]
            val, wt = items[j-1]
            taken[j-1] = 1
            i -= wt

    return result, taken






# ###############################################################
#
# IMPLEMENTATION Of above solution
#
# ################################################################


def solveIt(inputData):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    no_of_items = int(firstLine[0])
    capacity = int(firstLine[1])

    values = []
    weights = []

    for i in range(1, no_of_items+1):
        line = lines[i]
        parts = line.split()

        values.append(int(parts[0]))
        weights.append(int(parts[1]))

    no_of_items = len(values)
    items = zip(values, weights)

    value, taken = kptable(items, capacity)


    # prepare the solution in the specified output format
    outputData = str(value) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(str, taken))
    return outputData



import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        #choosebest = memoize(choosebest)
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

