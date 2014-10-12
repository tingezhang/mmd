#!/usr/bin/env python

import numpy as np
from loadgraph import loadDirectedGraph
from optparse import OptionParser
import rpdb
import sys


def computePageRank(graphfile, beta, epsilon):
    (nodelist, nodedict) = loadDirectedGraph(graphfile)

    if (None is nodelist) or (None is nodedict):
        return None

    # generate adjacent matrix
    size = len(nodelist)
    adjmat = np.zeros((size, size), dtype=int)

    for col, srcnode in enumerate(nodelist):
        for dstnode in nodedict[srcnode]:
            row = nodelist.index(dstnode)
            adjmat[row, col] = 1

    ranka = np.ones(size, dtype=np.float32) / size
    rankb = np.zeros(size, dtype=np.float32)

#    rpdb.set_trace()
    while True:
        # first round
        for dstidx, dstnode in enumerate(nodelist):
            # when out deg is not zero
            if 0 != len(nodedict[dstnode]):
                srcvector = adjmat[dstidx, :]
                for srcidx, linkflag in enumerate(srcvector):
                    if 1 == linkflag:
                        rankb[dstidx] = rankb[dstidx] \
                            + beta * ranka[srcidx] / len(nodedict[nodelist[srcidx]])

        # make up importance leaked out
        S = np.sum(rankb)
        rankb = rankb + np.ones(size, dtype=np.float32) * (1 - S) / size

        # compare
        rankdelta = np.fabs(rankb - ranka)
        if (np.amax(rankdelta) < epsilon):
            break

        ranka = rankb
        rankb = np.zeros(size, dtype=np.float32)

    return rankb


if '__main__' == __name__:
    parser = OptionParser(usage="usage: %prog [options] graphfilename",
                          version="%prog 1.0")
    parser.add_option("-b", "--beta", action="store", type="float", dest="beta",
                      default="0.85", help="beta for teleport")
    parser.add_option("-e", "--epsilon", action="store", type="float",
                      dest="epsilon", default="0.0000001",
                      help="epsilon for delta")

    (options, args) = parser.parse_args()

    print options
    print args

    if 1 != len(args):
        parser.error("wrong number of arguments")

    rank = computePageRank(args[0], options.beta, options.epsilon)

    print rank
