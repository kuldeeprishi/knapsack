# ####################################################
#
# Simple Solution to Knapsack Problem
# Using Branch and Bound
# Provides a Optimal Solution for even large lists
#
# ####################################################



#!/usr/bin/python
# -*- coding: utf-8 -*-

class node(object):
    def __init__(self, taken, profit, weight, level):
        self.taken = taken
        self.profit = profit
        self.weight = weight
        self.level = level
    def __str__(self):
        return '('+str(self.taken) +'=>'+str(self.profit)+', '+str(self.weight)+', '+str(self.level)+')'
    def __repr__(self):
        return '('+str(self.taken) +'=>'+str(self.profit)+', '+str(self.weight)+', '+str(self.level)+')'

def bnb_wrapper(l, cap):
    # create root node
    root = node([0 for i in xrange(len(l))], 0, 0,0)

    # set UPPER BOUND to bound of root
    ub = bound(root, cap, l)

    # set LOWER BOUND = 0
    lb = 0

    # set BEST VALUE = 0
    best = 0

    # BEST ITEMS = []
    best_items = []

    # create a queue and append root to it
    Q = [root]

    # WHILE ELEMENT IN QUEUE REPEAT FOLLOWING
    while Q:
        # pop first element from queue call it cur
        cur = Q.pop(0)

        # find children of cur [childrenof will return a list of children or None]
        children = childrenof(cur,l, cap)

        if children != None:
            for child in reversed(children): # reversed so as to maintain Q in proper order
                boc = bound(child, cap, l)   # find bound of child
                if boc <= ub and boc >= best and child.weight <= cap:
                    # add children to queue
                    Q = [child] + Q
        else:
            # set LOWER_BOUND = bound of cur
            lo = bound(cur, cap, l)
            if lo > best: # update best
                best = lo
                best_items = cur.taken # update best_items taken
    return best, best_items


def childrenof(n, l, cap):
    if len(l[n.level:]) == 0: # if no further element in list
        return None

    first = l[n.level:][0]  # take first element of list
    iof = l.index(first)    # find its index in list
    taken = n.taken[:]      # copy a list of taken element
    taken[iof] = 1          # update position of first element in new taken list

    # create first child with first element
    child1 = node(taken, n.profit+first[0], n.weight+first[1], n.level+1)

    # create second child without first element
    child2 = node(n.taken, n.profit, n.weight, n.level+1)

    # return list of childs
    return [child1, child2]

BOUND_CACHE = {}
def bound(node, cap, l):
    n = len(l)
    totwt = 0
    if node.weight > cap: # if cant fit element then return bound of 0
        return 0
    elif (node, cap) in BOUND_CACHE:
        return BOUND_CACHE[(node, cap)]
    else:
        est = node.profit   # est is at least equal to profit of prev. node
        totwt = node.weight # same for total weight
        j = node.level      # j for looping through rest of list

        while (j < n and totwt + l[j][1] <= cap): # loop remaining list keeping in view that totwt dont exceed cap
            totwt = totwt + l[j][1]
            est += l[j][0]
            j+=1
        k = j
        if k < n:   # if still space left in knapsack add fraction of next element
            est = est + int((cap - totwt) * (float(l[k][0])  / l[k][1]))
        BOUND_CACHE[(node, cap)] = est
        return est


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

    items_list = []
    #print 'buildingg list'
    for i in xrange(1, no_of_items+1):
        line = lines[i]
        parts = line.split()
        items_list.append((int(parts[0]), int(parts[1]), i-1))
    #print 'done building list\n'

    #print 'sorting'
    items_list.sort(key=lambda tup: float(tup[0])/tup[1], reverse = True)
    #print 'done sorting\n'

    #print 'finding solution'
    value, item_taken = bnb_wrapper(items_list, capacity)
    #print 'found solution\n'

    #print 'preparing answer'
    taken = [0 for i in xrange(no_of_items)]
    for i in xrange(len(item_taken)):
        if item_taken[i] == 1:
            taken[items_list[i][2]] = 1
    #print 'done preparing answer'


    # prepare the solution in the specified output format
    outputData = str(value) + ' ' + str(1) + '\n'
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


















