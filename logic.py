i=0
j=0
def valid(m,i,j,val):
    for it in range(9):
        if m[i][it]==val:
            return False
        if m[it][j]==val:
            return False
    it=i//3
    jt=j//3
    for i in range(it*3,it*3+3):
        for j in range (jt*3,jt*3+3):
            if m[i][j]==val:
                return False
    return True        
def solve(m,i,j):
    
    while m[i][j]!=0:
        if i<8:
            i+=1
        elif i==8 and j<8:
            i=0
            j+=1
        elif i==8 and j==8:
            return True
    for it in range(1,10):
        if valid(m,i,j,it)==True:
            m[i][j]=it
            
            if solve(m,i,j)==1:
                return True
            else:
                m[i][j]=0
    return False           

#m =[[4,0,0,8,0,5,0,0,9],
#       [0,0,5,0,0,0,0,8,6],
#	   [0,0,0,0,0,0,0,0,0],
#	   [0,7,0,0,0,9,5,0,0],
#       [3,0,0,0,5,0,0,0,0],
#	   [0,0,6,0,7,0,1,0,0],
#	   [0,3,0,0,0,0,0,0,4],
#	   [5,0,0,0,3,7,2,0,0],
#	   [0,6,0,9,0,0,0,0,0]]
#if solve(m,0,0)==True:
#    print(m)