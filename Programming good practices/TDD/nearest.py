def nearest_square(num):
    """
    Return the nearest perfect square that is less than or equal to the num. 
    """
    
    root = 0
    while (root+1)**2 <= num:
        root+=1
    return root**2    

# Running python -m pytest on the terminal 
# python -m is for running modules. 
print(nearest_square(8))