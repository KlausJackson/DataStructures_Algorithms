def bubble_sort(list_to_sort):
    for i in range(0, len(list_to_sort) - 1):
        for j in range(0, len(list_to_sort) - i - 1):
            if list_to_sort[j] > list_to_sort[j + 1]:
                temp = list_to_sort[j]
                list_to_sort[j] = list_to_sort[j + 1]
                list_to_sort[j + 1] = temp
                

list0 = input("List to sort: ")
list1 = list(map(float, list0.strip().split()))       
                
bubble_sort(list1)
list1 = ' '.join(map(lambda x: str(int(x)) if x.is_integer() else str(x), list1))
print("List after sorting: ", list1)                