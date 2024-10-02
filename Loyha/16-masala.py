list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]
list4 = [10,11,12]

lists = [list1, list2, list3, list4]

max_list = max(lists, key=sum)

print(max_list)
