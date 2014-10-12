import sys
import os
import numpy as np


'''
load a directed graph adjacent matrix from a file
the representation of directed graph is as the following:
NODE1: NODEX, NODEY
NODE2: NODEA, NODEB
NODE3:
...
NODEN: NODEE, NODEF
'''


def loadDirectedGraph(filename):
    if not os.path.isfile(filename):
        print "invalid file path %s" % filename
        return (None, None)

    # read
    nodedir = {}
    allnodes = []
    nodefile = open(filename)
    nodelist = nodefile.readlines()

    for nodeline in nodelist:
        items = nodeline.split(':', 1)
        srcnode = items[0].strip()
        dstnodelist = items[1].strip().split(',')
        dstnodes = []
        for dstnode in dstnodelist:
            if len(dstnode) > 0:
                dstnodes.append(dstnode.strip())
        nodedir[srcnode] = dstnodes
        allnodes.append(srcnode)

    # verify
    for srcnode in allnodes:
        for dstnode in nodedir[srcnode]:
            if dstnode not in allnodes:
                print "dstnd :%s for srcnd: %s not valid" % (dstnode, srcnode)
                return (None, None)
    return (allnodes, nodedir)


def loadGraphAdjacentMatrix(filename):
    (allnodes, nodedir) = loadDirectedGraph(filename)

    if (None is allnodes) or (None is nodedir):
        return None

    # generate adjacent matrix
    size = len(allnodes)
    adjmat = np.zeros((size, size), dtype=int)

    for col, srcnode in enumerate(allnodes):
        for dstnode in nodedir[srcnode]:
            row = allnodes.index(dstnode)
            adjmat[row, col] = 1

    return adjmat


def loadStochasticAdjacentMatrix(filename):
    (allnodes, nodedir) = loadDirectedGraph(filename)

    if (None is allnodes) or (None is nodedir):
        return None

    # generate adjacent matrix
    size = len(allnodes)
    adjmat = np.zeros((size, size), dtype=np.float32)

    for col, srcnode in enumerate(allnodes):
        dstcnt = len(nodedir[srcnode])
        for dstnode in nodedir[srcnode]:
            row = allnodes.index(dstnode)
            adjmat[row, col] = 1.0 / dstcnt

    return adjmat


def test():
    output = open('test.g', 'w')
    output.write("A: B, C, D\n")
    output.write("B: E, F, H\n")
    output.write("C: \n")
    output.write("D: A, E, F, G, H\n")
    output.write("E: B, C\n")
    output.write("F: C, G\n")
    output.write("G: A, D, E\n")
    output.write("H: C, D, F\n")
    output.close()

    mat = loadStochasticAdjacentMatrix('test.g')
    print mat

    mat = loadGraphAdjacentMatrix('test.g')
    print mat

if '__main__' == __name__:
    test()
