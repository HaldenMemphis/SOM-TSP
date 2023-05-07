import math
import matplotlib.pyplot as plt
import numpy as np


## Dynamic Planning Method
class DP(object):
    def __init__(self, num_city, num_total, iteration, data):
        self.num_city = num_city
        self.location = data
        self.dis_mat = self.compute_dis_mat(num_city, data)

    # Calculate the distance between different cities
    def compute_dis_mat(self, num_city, location):
        dis_mat = np.zeros((num_city, num_city))
        for i in range(num_city):
            for j in range(num_city):
                if i == j:
                    dis_mat[i][j] = np.inf
                    continue
                a = location[i]
                b = location[j]
                tmp = np.sqrt(sum([(x[0] - x[1]) ** 2 for x in zip(a, b)]))
                dis_mat[i][j] = tmp
        return dis_mat

    # Calculate the path length, goback: whether to calculate the path back to the start point
    def compute_pathlen(self, path, dis_mat, goback=True):
        try:
            a = path[0]
            b = path[-1]
        except:
            import pdb
            pdb.set_trace()
        if goback:
            result = dis_mat[a][b]
        else:
            result = 0.0
        for i in range(len(path) - 1):
            a = path[i]
            b = path[i + 1]
            result += dis_mat[a][b]
        return result

    # Run DP
    def run(self):
        restnum = [x for x in range(1, self.num_city)]
        tmppath = [0]
        tmplen = 0
        while len(restnum) > 0:
            c = restnum[0]
            restnum = restnum[1:]
            if len(tmppath) <= 1:
                tmppath.append(c)
                tmplen = self.compute_pathlen(tmppath, self.dis_mat)
                continue

            insert = 0
            minlen = math.inf
            for i, num in enumerate(tmppath):
                a = tmppath[-1] if i == 0 else tmppath[i - 1]
                b = tmppath[i]
                tmp1 = self.dis_mat[c][a]
                tmp2 = self.dis_mat[c][b]
                curlen = tmplen + tmp1 + tmp2 - self.dis_mat[a][b]
                if curlen < minlen:
                    minlen = curlen
                    insert = i

            tmppath = tmppath[0:insert] + [c] + tmppath[insert:]
            tmplen = minlen
        return self.location[tmppath], tmplen
