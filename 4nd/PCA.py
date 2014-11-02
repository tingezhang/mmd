#!/usr/bin/env python

import numpy as NP
from numpy import linalg as LA

M = NP.array([[1,1], [2,2], [3,4]])
MT = NP.transpose(M)

T = NP.dot(MT, M)

print M
print MT
print T

W,V = LA.eig(T)

print W
print V

VP = NP.transpose(V[:,1])
print VP


value = NP.dot(M, VP)

print value



