list = [1,2,3,4,5,6,7,8,9]

list1 = [i for i in list]
list2 = [i*2 for i in list if i%2==0]
list3 = [(x,y) for x in "abcd" for y in "abcd"]

print(list1,list2,list3,sep=";")