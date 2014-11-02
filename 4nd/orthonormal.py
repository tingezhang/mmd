#!/usr/bin/env python


import numpy as NP


M = NP.array([[-0.937, 0.312, 0.156],
              [-0.702, 0.117, 0.702],
              [0.485, -0.485, 0.728],
              [0.954, 0.728, -0.682]])

MT = NP.transpose(M)

A = NP.dot(M, MT)

print A

Y = NP.transpose(NP.array([2, 3, 6]))
B = NP.dot(M, Y)
print B


