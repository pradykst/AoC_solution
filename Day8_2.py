from collections import defaultdict
import math

def parse_points(path):
    points=[]


    with open(path,"r") as f:
        for line in f:
            line=line.strip()


            if not line:
                continue


            x,y,z=map(int,line.split(","))


            points.append((x,y,z))

    return points



def sq_dist(a,b):
    dx=a[0]-b[0]
    dy=a[1]-b[1]
    dz=a[2]-b[2]

    return dx*dx+dy*dy+dz*dz

class DSU:
    def __init__(self,n):
        self.parent=list(range(n))
        self.size=[1]*n

    def find(self,x):
        while self.parent[x]!=x:
            self.parent[x]=self.parent[self.parent[x]]
            x=self.parent[x]
        return x
    
    def union(self,a,b):
        ra=self.find(a)
        rb=self.find(b)

        if ra==rb:
            return False
        
        if self.size[ra]<self.size[rb]:
            ra,rb=rb,ra
        
        self.parent[rb]=ra
        self.size[ra]+=self.size[rb]

        return True


def last_connection_x_product(path="input8.txt"):
    points=parse_points(path)

    n=len(points)

    edges=[]

    for i in range(n):
        pi=points[i]

        for j in range(i+1,n):
            d=sq_dist(pi,points[j])

            edges.append((d,i,j))

    edges.sort(key=lambda x:x[0])

    dsu=DSU(n)

    components=n
    last_u=last_v=None

    for d,i,j in edges:
        if dsu.union(i,j):
            components-=1
            last_u,last_v=i,j
            if components==1:
                break
    

    if last_u is None or last_v is None:
        raise RuntimeError("graph never became fully connected")

    
    x1=points[last_u][0]
    x2=points[last_v][0]
    return x1*x2


if __name__=="__main__":
    print(last_connection_x_product("input8.txt"))
