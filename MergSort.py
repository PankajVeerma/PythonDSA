def merg_sort(list1):
    if len(list1)>1:
        mid = len(list1)//2
        left_list = list1[:mid]
        right_list = list1[mid:]
        merg_sort(left_list)
        merg_sort(right_list)
        #Merging
        i,j,k=0,0,0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
               list1[k ]= left_list[i]
               i+=1
              
            else:
               list1[k ]= right_list[j]
               j+=1
            k+=1  
        while i<len(left_list):
            list1[k]=left_list[i]
            i+=1
            k+=1       
        while j<len(right_list):
            list1[k]=right_list[j]
            j+=1
            k+=1       

l = [32,54,67,39,56,87,454,34]        
merg_sort(l)   
print(l)     