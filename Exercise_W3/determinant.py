
mat=[
    [1,1,2],
    [2,0,1],
    [6,2,1],
    ] 
def determinant(mat,n):
    if n==2:
       kahad= mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0] 
       return kahad
    
    sum=0
    for i in range(n):
        mat1=[]
        mat2=[]
        for j in range(1,n):
            for k in range(n):
                if k!=i:
                    mat1.append(mat[j][k])   
            mat2.append(mat1)    
            mat1=[]
        print(mat2)     
        sum+=(-1)**i*mat[0][i]*determinant(mat2, n-1) 
        print(sum)
    return sum    
     
print(determinant(mat,3))                  

