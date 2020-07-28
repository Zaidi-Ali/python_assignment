list1 = [1,2,3,4,5,6,7,8]

list2 = ["a" , "b" , "c" , "d" , "e"]

list_Dict = {}

for lists in list1:
    for list_it in list2:
        list_Dict[lists] = list_it
        list2.remove(list_it)
        break

print("Combined List:\n",list_Dict)
