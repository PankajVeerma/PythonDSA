def selection_sort(list): 
    for i in range(len(list)-1):
        min_index=i
        for j in range(i+1,len(list)):
            if list[j]<list[min_index]:
                min_index=j
        list[i],list[min_index]=list[min_index],list[i]        

l = [32,54,67,39,56,87,454,34]        
selection_sort(l)
print(l)        