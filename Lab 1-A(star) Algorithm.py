def astaralgo(startnode,endnode):
    open_set=set((startnode))
    closed_set=set()
    g={}
    parent={}
    parent[startnode]=startnode
    g[startnode]=0
   
   
    while len(open_set)>0:
        n=None
       
        for v in open_set:
            if n==None or g[v]+heu[v]<g[n]+heu[n]: #to select the node
                n=v
               
        if n==endnode or graph[n]==None:
            pass
        else:
            for (m,weight) in get_adjacent(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    g[m]=g[n]+weight
                    parent[m]=n
                else:
                    if g[m]>g[n]+weight:
                        g[m]=g[n]+weight
                        parent[m]=n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
                       
        
        if n==endnode:
            path=[]

            while parent[n]!=n:
                path.append(n)
                n=parent[n]

            path.append(startnode)
            path.reverse()

            print("---path found---")
            return path
        
        
        open_set.remove(n)
        closed_set.add(n)
    print('Path not found')
                       
                       
    print('open_set',open_set)
    print('parent',parent)
    print('distance g',g)
           
               
               
def get_adjacent(v):
    if v in graph:
        return graph[v]  #fetches the details from node
    else:
        None
   
graph={
    'S':[('A',1),('G',12)],
    'A':[('B',3),('C',1)],
    'B':[('D',3)],
    'C':[('D',1),('G',2)],
    'D':[('G',3)],
    'G':None
}

heu={'S':4,'A':2,'B':6,'D':3,'C':2,'G':0}

astaralgo('S','G')
