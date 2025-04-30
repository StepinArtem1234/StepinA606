n = int(input())
trust = [[1,3], [2,3]]
outin = [[0,0] for i in range(n)]
for i in trust:
    outin [i[0]-1][0]+=1
    outin [i[1]-1][1]+=1
index = -1
if [0,n-1] in outin:
    index = outin.index([0,n-1])+1
print(index)
