
import operator
import functools

mat1=[
    [1,0,1],
    [0,2,1],
    [0,3,2],
    [0,0,1]
]
mat2=[
    [0,1,2,3],
    [2,0,1,2],
    [1,0,1,2]
    ]


satr_mat1=len(mat1)
sotoon_mat1=len(mat1[0])
print("str1:",satr_mat1,"sotoon2:",sotoon_mat1)

satr_mat2=len(mat2)
sotoon_mat2=len(mat2[0])                  
print("str2:",satr_mat2,"sotoon2:",sotoon_mat2)





if  satr_mat1==sotoon_mat2 :
    my_mat = []
    for i in range(satr_mat1):
        list1=[]
        for j in range(sotoon_mat2):
            list2=[]
            for k in range(sotoon_mat1):
                list2.append(mat1[i][k]*mat2[k][j])      
            list1.append(functools.reduce(operator.add,list2))
        my_mat.append(list1)    
    print(my_mat)    