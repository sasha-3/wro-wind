# 2d coord operations

from math import sqrt, acos, sin, cos

# pt2 - pt1
def diff(pt1, pt2):
    return pt2[0] - pt1[0], pt2[1] - pt1[1]

def add(pt1, pt2):
    return pt1[0] + pt2[0], pt1[1] + pt2[1]

# (pt2 + pt1) // 2
def avg(pt1, pt2):
    return (pt2[0] + pt1[0]) // 2, (pt2[1] + pt1[1]) // 2

# distance between two pts
def dist(pt1, pt2):
    d = diff(pt1, pt2)
    return sqrt(d[0] * d[0] + d[1] * d[1])

# * const
def mul(pt, n1, n2):
    return (pt[0] * n1, pt[1] * n2)

def split(arr):
    return (arr[0], arr[1]), (arr[2], arr[3])

# implicit casting to integer
def toInt(pt):
    return tuple([int(x) for x in pt])

def length(vec):
    return sqrt(vec[0]**2 + vec[1]**2)

def angle_between(vec1, vec2):
    return acos((vec1[0]*vec2[0] + vec1[1]*vec2[1])/(length(vec1)*length(vec2)))

def rotate_vector(vec, angle):
    cs = cos(angle)
    sn = sin(angle)
    return (vec[0]*cs - vec[1]*sn, sn*vec[0] + cs*vec[1])