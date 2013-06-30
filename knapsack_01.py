# ####################################################
#
# Simple Solution to Knapsack Problem
# Using Recursion
# Works best when len of list is small
#
# ####################################################


def O(items, k):
    """ Input list of items in shown format  and capacity of knapsack (integer) k
        Input = O([(value, weight),...], k)

        Output: Best/Max value that can fit in knapsack with given capacity k and list of items to be taken
        Output = (Best value, [(value, weight),....])
        """
    if len(items) == 0 or k ==0:
        return [0, []]
    # dont take item 1
    v1, t1 = O(items[1:], k)
    # take item 1
    v2, t2 = O(items[1:], k-items[0][1])  # since taking first item so k is reduced by weight of item 1
    v2 += items[0][0]   # append value of first item
    t2.append(items[0]) # append item 1 to list of taken items

    if v2 > v1 and items[0][1] <= k:  # if value with taking item1 is > without taking item 1
        return (v2, t2)               # and weight of item 1 is less than capacity of knapsack
    else:
        return (v1, t1)


# Test case 1:   4 items
i1 = [(8, 4), (10, 5), (15, 8), (4, 3)]
n1 = 4
w1 = 11

# Test case 2:   19 items
i2 = [(1945, 4990), (321, 1142), (2945, 7390), (4136, 10372), (1107, 3114), (1022, 2744), (1101, 3102), (2890, 7280), (962, 2624), (1060, 3020), (805, 2310), (689, 2078), (1513, 3926), (3878, 9656), (13504, 32708), (1865, 4830), (667, 2034), (1833, 4766), (16553, 40006)]
n2 = 19
w2 = 31181


print 'With 4 items best answer is',O(i1, w1)
print "=============================="
print 'With 19 items best answer is',O(i2, w2)