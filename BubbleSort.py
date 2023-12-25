def bubble_sort(data_list):
    for i in  range(1,len(data_list)):
        for j in range(0,len(data_list)-i):
            if data_list[j]>data_list[j+1]:
              data_list[j], data_list[j+1]= data_list[j+1],data_list[j]
                   
l = [32,54,67,39,56,87,454,34]        
bubble_sort(l)
print(l)




def modifyed_bubble_sort(data_list):
    flag=False
    for i in  range(1,len(data_list)):
        flag=False
        for j in range(0,len(data_list)-i):
            if data_list[j]>data_list[j+1]:
              data_list[j], data_list[j+1]= data_list[j+1],data_list[j]    
              flag=True
        if not flag:
            break      
l = [32,54,67,39,56,87,454,34]        
modifyed_bubble_sort(l)
print(l)


    