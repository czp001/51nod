'''
https://segmentfault.com/a/1190000004457595
'''
class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

class Vector(object):
    def __init__(self, start_point, end_point):
        self.start, self.end = start_point, end_point
        self.x = end_point.x - start_point.x
        self.y = end_point.y - start_point.y

def vector_product(vectorA, vectorB):
    return vectorA.x * vectorB.y - vectorB.x * vectorA.y

def is_intersected(A, B, C, D):
    AC = Vector(A, C)
    AD = Vector(A, D)
    BC = Vector(B, C)
    BD = Vector(B, D)
    if (vector_product(AC, AD) * vector_product(BC, BD) <= 0) \
        and (vector_product(AC, BC) * vector_product(AD, BD) <= 0):
        return 'Yes'
    else:
        return 'No'

t=input()
for _ in range(t):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, raw_input().strip().split(' '))
    A, B = Point(x1, y1), Point(x2, y2)
    C, D = Point(x3, y3), Point(x4, y4)
    print is_intersected(A, B, C, D)
