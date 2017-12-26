# coding:utf-8
# 啥的
class Vector:
    def __init__(self, index, dist):
        self.index = index
        self.dist = dist
    def printVector(self):
        print "index = ", self.index, "distance = ", self.dist