fruit_list=[
    {'name':'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
    {'name':'mango', 'shape': 'square', 'mass': 150, 'volume': 120}, 
    {'name':'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
    {'name':'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250}]
def fruits():
    my_dict = {}
    for fruit in fruit_list:
        if fruit['shape'] == 'sphere' and 300 <= fruit['mass'] <= 600 and 100 <= fruit['volume'] <= 500:
            if fruit['name'] in my_dict:
                my_dict[fruit['name']] += 1
            else:
                my_dict[fruit['name']] = 1
    return my_dict 
print(fruits())   