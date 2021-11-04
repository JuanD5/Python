#%%
# Soy libre por N dias consecutivos 
# Cada locación se identifica con un número de 0 a N-1 indices de la lista A 
# A[K] es el identificador de la locación el cual es el destino del día K 

# Hay que encontrar la longitud del mínimo subarray que contenga todos los números de las visitas. 

A = [7,5,2,7,2,7,4,7]

A_1 =[2,1,1,3,2,1,1,3]


def vacations(arr_vacation):
    
    l,r = 0, 1
    
    num_places = list(set(arr_vacation))
    
    min_len = len(arr_vacation)
    
    while r <= len (arr_vacation):
        
        subarr = arr_vacation[l:r]
        
        result = all(elem in subarr for elem in num_places)
        
        if not result:
            
            r+=1
        
        else : 
            
            min_len = min(min_len,len(subarr))  
            
            l +=1  
        
    return min_len    


vacations([2,1,1,3,2,1,1,3])            
    