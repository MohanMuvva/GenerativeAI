list=[]
for i in range(1,20):
    list.append(i)
print(list)
list[0]=4
print(list)
list.insert(0,4)
print(list)
list.pop(3)
print(list)
removed_item=list.pop(4)
print("removed_item:",removed_item)
print(list)
retrieved_item=list.pop(4)
print("retrieved_item:", retrieved_item)
print(list)
removed_item1= list.remove(2)  #not valid
print("removed_item1:", removed_item1)
print(list)
fruits = ('apple', 'banana', 'cherry', 'banana')
print(fruits[1])
print(len(fruits))
fruits=()
for i in range(12): 
    fruits.append(i) #not valid 