import heapq
from collections import defaultdict

K=1000

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


    


def get_k_smallest_edges(points,k=K):
    n=len(points)


    heap=[]


    for i in range(n):
        pi=points[i]

        for j in range(i+1,n):

            d=sq_dist(pi,points[j])


            if len(heap)<k:
                heapq.heappush(heap,(-d,i,j))

            else:
                largest_d=-heap[0][0]

                if d<largest_d:
                    heapq.heapreplace(heap,(-d,i,j))

    edges=[(-neg_d,i,j) for neg_d,i,j in heap]
    edges.sort(key=lambda x:x[0])

    return edges



def solve(path="input8.txt",k=1000):
    points=parse_points(path)

    n=len(points)

    edges=get_k_smallest_edges(points,k)

    dsu=DSU(n)


    for _,i,j in edges:
        dsu.union(i,j)

    comp_sizes=defaultdict(int)

    for i in range(n):
        comp_sizes[dsu.find(i)]+=1

    sizes=sorted(comp_sizes.values(),reverse=True)

    if len(sizes)<3:
        result=1
    
        for s in sizes:
            result*=s
        return result


    return sizes[0]*sizes[1]*sizes[2]

if __name__=="__main__":
    print(solve("input8.txt",1000))

            
    



