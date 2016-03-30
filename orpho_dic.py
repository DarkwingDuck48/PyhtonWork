d=int(input())
i=0
dic=[]
output=[]
while i<d:
    a=input()
    a=a.lower()
    dic.append(a)
    i+=1
l=int(input())
i=0
while i<l:
    strok=input()
    strok=strok.lower()
    strok=strok.split(" ")
    for j in range (0,len(strok)):
        if strok[j] not in dic:
            output.append(strok[j])
    i+=1
for c in output:
    print (c)
