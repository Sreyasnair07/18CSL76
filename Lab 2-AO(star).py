class graph:
    def __init__(self,graph,hnodelist,startnode):
        self.graph=graph
        self.H=hnodelist
        self.start=startnode
        self.parent={}
        self.status={}
        self.solutiongraph={}
        
    def applyaostar(self):
        self.aostar(self.start,False)
    def getneighbors(self,v):
        return self.graph.get(v,'')
    
    def getstatus(self,v):
        return self.status.get(v,0)
    def setstatus(self,v,val):
        self.status[v]=val
    def geth(self,H):
        return self.H.get(H,0)
    
    def seth(self,n,value):
        self.H[n]=value
    
        
    def printsolution(self):
        print(self.solutiongraph)
        
    def findmincost(self,v):
        minimumcost=0
        costtochild={}
        costtochild[minimumcost]=[]
        flag=True
        for nodeinfotuplelist in self.getneighbors(v):
            cost=0
            nodelist=[]
            for c, weight in nodeinfotuplelist:
                cost=cost+self.geth(c)+weight
                nodelist.append(c)
                
            if flag==True:
                minimumcost=cost
                costtochild[minimumcost]=nodelist
                flag=False
            else:
                if minimumcost>cost:
                    minimumcost=cost
                    costtochild[minimumcost]=nodelist
        
        return minimumcost,costtochild[minimumcost]
    
    def aostar(self,v,backtracking):
        print("Heuristic Values:",self.H)
        print("solution graph:",self.solutiongraph)
        print("Processing node:",v)
        print("--------------------------------------------------------------------------------------")
        
        if self.getstatus(v)>=0:
            minimumcost,childnodelist=self.findmincost(v)
            self.seth(v,minimumcost)
            self.setstatus(v,len(childnodelist))
            solved=True
            for childnode in childnodelist:
                self.parent[childnode]=v
                if self.getstatus(childnode)!=-1:
                    solved=solved & False
        
        if solved==True:
            self.setstatus(v,-1)
            self.solutiongraph[v]=childnodelist
        if v!=self.start:
            self.aostar(self.parent[v],True)
            
        if backtracking==False:
            for childnode in childnodelist:
                self.setstatus(childnode,0)
                self.aostar(childnode,False)
h1={'A':1,'B':6,'C':2,'D':12,'E':2,'F':1,'G':5,'H':7,'I':7,'J':1}
graph1={
        'A':[[('B',1),('C',1)],[('D',1)]],
        'B':[[('G',1)],[('H',1)]],
        'C':[[('J',1)]],
        'D':[[('E',1),('F',1)]],
        'G':[[('I',1)]]
        }
g1=graph(graph1,h1,'A')
g1.applyaostar()
g1.printsolution()
from pprint import pprint
"""pprint("huristic values  ",G1.H)
pprint("solution Graph  ",G1.solutionGraph)"""
print("\nhuristic values  ",g1.H)
print("\nsolution Graph  ",g1.solutiongraph)
