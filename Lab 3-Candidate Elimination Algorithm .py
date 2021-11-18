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




