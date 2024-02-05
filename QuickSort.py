#divide and conquer methode
#taking pivote element
def quick_sort(list1):
    if len(list1)<=1:
        return list1
    else:
        pivot=list1[0]
        lesser=[x for x in list1[1:] if x <= pivot ]   #using list comprihension
        greater=[x for x in list1[1:] if x > pivot ]
        return quick_sort(lesser) +[pivot]+ quick_sort(greater)



l = [32,54,67,39,56,87,454,34]        
l = quick_sort(l)   
print(l)     