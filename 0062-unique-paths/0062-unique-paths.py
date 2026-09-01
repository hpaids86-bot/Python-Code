class Solution(object):
    def uniquePaths(self, m, n):
        c=[1]*n
        p=[1]*n
        p1=1
        for i in range(1,m):
            p1=1
            for j in range(1,n):
                c[j]=p1+p[j]
                p1=c[j]
                p[j]=c[j]
        return c[n-1]
        