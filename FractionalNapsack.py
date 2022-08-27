weight=[100, 4, 20, 30]
value=[60, 40, 120, 150]
we_val_dict=dict(zip(weight,value))
we_co_val_dict={}
for w,v in we_val_dict.items():
    we_co_val_dict[w]=[v/w,v]
sorted_dict=dict(sorted(we_co_val_dict.items(), key =lambda kv:(kv[1], kv[0]),reverse=True))



weight_capacity=50
napsack_Value = 0
for i in sorted_dict:
    Wt = i
    Val = sorted_dict[i][1]
    if weight_capacity - Wt >= 0:
        weight_capacity -= Wt
        napsack_Value += Val
    else:
        fractional = weight_capacity / Wt
        napsack_Value += Val * fractional
        break

    
print('napsack value:',napsack_Value)