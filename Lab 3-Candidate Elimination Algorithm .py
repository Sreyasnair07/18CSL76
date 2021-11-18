#!/usr/bin/env python
# coding: utf-8

# In[15]:


import csv
file=open(r'C:\Users\Admin\OneDrive\Desktop\file.csv')
data=list(csv.reader(file))[1:]
concepts=[]
targets=[]

for i in data:
    concepts.append(i[:-1])
    targets.append(i[-1])
    
sh=['0']*len(concepts[0])
gh=[['?' for i in range (len(sh))]for i in range (len(sh))]
for i,instance in enumerate(concepts):
    if targets[i]=="Yes":
        for x in range (len(sh)):
            if sh[x]=='0':
                sh[x]=instance[x]
            elif instance[x]!=sh[x]:
                sh[x]='?'
                gh[x][x]=sh[x]
                
    if targets[i]=="No":
        for x in range(len(sh)):
            if instance[x]!=sh[x]:
                gh[x][x]=sh[x]
            else:
                gh[x][x]='?'
                
                
indices=[i for i,val in enumerate(gh) if val==['?','?','?','?','?','?']]
for i in indices:
    gh.remove(['?','?','?','?','?','?'])
    
print("final specifics:",sh,sep="\n")
print("final general:",gh,sep="\n")


# In[ ]:




Vvvvvvvv


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
                       
            if n==None:
                print("Path does not exists")
               
            if n==endnode:
                path=[]
               
                while parent[n]!=n:
                    path.append(n)
                    n=parent[n]
                   
                path.append(startnode)
                path.reverse()
               
                print("---path found---")
                for x in path:
                    print(x,'->',end='')
                       
        open_set.remove(n)
        closed_set.add(n)
                       
                       
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
