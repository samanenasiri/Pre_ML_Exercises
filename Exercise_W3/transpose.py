mat1=[
    [4,5,3],
    [0,2,1],
    [4,2,6],
    [4,5,2]
]


satr_mat1=len(mat1)
sotoon_mat1=len(mat1[0])
print("str mat1 :",satr_mat1,"sotoon mat1:",sotoon_mat1)



my_transpose=[[0 for z in range(satr_mat1)] for l in range(sotoon_mat1)]
print(my_transpose)

satr_my_transpose=len(my_transpose)
sotoon_my_transpose=len(my_transpose[0])                  
print("str my_transpose:",satr_my_transpose,"sotoon my_transpose:",sotoon_my_transpose)


for i in range(satr_mat1):
    for j in range(sotoon_mat1):
            my_transpose[j][i]=mat1[i][j]
print(my_transpose)