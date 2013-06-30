def recursive_dfs(graph, start, path=[]):
  '''recursive depth first search from start'''
  path=path+[start]
  for node in graph[start]:
    if not node in path:
      path=recursive_dfs(graph, node, path)
  return path

def iterative_dfs(graph, start, path=[]):
  '''iterative depth first search from start'''
  q=[start]
  while q:
    v=q.pop(0)
    if v not in path:
      path=path+[v]
      q=graph[v]+q
  return path

def iterative_bfs(graph, start, path=[]):
  '''iterative breadth first search from start'''
  q=[start]
  while q:
    v=q.pop(0)
    if not v in path:
      path=path+[v]
      q=q+graph[v]
  return path

'''
   +---- A
   |   /   \
   |  B--D--C
   |   \ | /
   +---- E
'''
graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
print 'recursive dfs ', recursive_dfs(graph, 'A')
print 'iterative dfs ', iterative_dfs(graph, 'A')
print 'iterative bfs ', iterative_bfs(graph, 'A')





best = 0
take = [0]

def branch(l, k):
    global best
    best = min(e[0] for e in l)
    est = sum(e[0] for e in l)
    #print 'estimated answer', est
    n = node(0, k, est)

    def bb(n, l, taken = []):
        global best
        global take
        #print n, l, best
        if len(l) == 1:
            #print best
            best = max(best, n.value)
                #print 'best answer so far', best, 'and taken item', take
            #print best, take
            return (best, take)

        first = l[0]
        rest = l[1:]
        # take item 1
        feasible = n.room >= first[1] and n.est > best
    ##    print 'feasibility with item', first, '=', feasible

        if feasible:
            #print 'taking item 1 therefore appending 1 to taken'
            taken.append(1)
            return bb(node(n.value+first[0], n.room - first[1], n.est), rest, taken = taken)
            #print 'result1 is',result1

        # dont take item 1

##        print 'here n.est =',n.est, 'and best=', best
        feasible = n.est >= best or n.room >= first[1]

    ##    print 'feasibility with rest item', rest, '=', feasible
        if feasible and n.est > best:
            taken.append(0)
            #print 'not taking item 1 therefore appending 0 to taken'
            return bb(node(n.value, n.room, n.est - first[0]), rest, taken = taken)
            #print 'result2 is',result2


    return bb(n, l)