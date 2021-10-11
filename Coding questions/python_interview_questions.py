# # print prime numbers between 100 and 200 

for num  in range(100,200):
    for i in range(2,num):
        if all( num%i !=0 for i in range(2,num)):# si al dividir todos los números desde 2 hasta ese número su modulo es diferente de 0 entonces será un número primo    
            print(num)
        
        

# # write a function than sorts the elements on a list 

datalist = [ 0,24,38,59,12,5,101]
arreglo = []

def sort_function():
    while datalist:
        minimum = datalist[0]
        for x in datalist:
            if x > minimum:
                minimum = x 
        arreglo.append(minimum)
        datalist.remove(minimum)
    return arreglo 



# # write a code for print the fibonacci series 


def F(n_terms):
    
    if n_terms <= 0:
        return 0
    elif n_terms == 1: 
        return 1 
    else: return F(n_terms-1)+F(n_terms-2)

for i in range(0,12):
    print(F(i))


c = [0,12,24,48,60,72]

def reverse(l):
    return l[::-1] # esto significa toma todos los elementos desde el principio hasta el final y devuelvelos en reversa (-1) 
reverse(c)
    

# function that returns if a word is a palindrome or not 

pa_1 = "madam"
pa_2 = "madami"

def palindrome(my_string):
    if my_string == my_string[::-1]:
        return print("its a palindrome")
    else :
        return print( "its not a palindrome")

palindrome(pa_1)        



# Function that returns a set of duplicates of a list 

my_list = [1,1,2,4,4,5,7,9,10,10]
aux = []
for i in my_list :
    if my_list.count(i)>1:
        aux.append(i)
    b = set(aux) 
print(b)       


# function that returns the number of words in a sentence 

sentence = " i still love you"
print(len(sentence.split()))


# given an array function that returns a given element (x) in the array  
def my_search(my_array,x):
    for i in range(len(my_array)):
        if my_array[i] == x:
            return print("the position of the number is:", i)
    print(" the element is not in the list")


arr = [2,5,6,7,8]
num = 8
my_search(arr,num)


# write a program which extracts digits from a string 

test_string = "bc98745dc"

res = ''.join(filter(lambda x: x.isdigit(), test_string)) # con la función lambda revisamos si cierta posición dentro del string es un dígito 

# la función de filter filtra una secuencia en este caso el test_string  con ayuda de la función lambda la cual checa si el elemento es verdadero o falso.
# Esta función va a pasar por cada posición del string y evaluará si es un dígito o no.  

print(res)

# function that removes the duplicates of a string. 
def remove_duplicates(any_string):
    for i in any_string:
        if any_string.count(i)>1:
            aux = any_string.replace(i,'')
            any_string = aux     
    return any_string       
            

carac = "abbbcjeeedad"
new_string = remove_duplicates(carac)    
print (new_string)

#%%
best_num1 = 0
best_num2 = 0
def mysum (arr_1,arr2,target):
    for i in arr_1:
        for j in arr2:
            suma = i + j
            if (target-suma)<=1:
                best_num1 = i
                best_num2 = j 
    return (best_num1,best_num2)            

arr = [3,5,6,7,9,8]
arr_t = [6,5,2,3,10,14]
tar = 20

(num1 ,num2 )= mysum(arr,arr_t,tar)
print(num1)
print(num2)

#%% return the largest range that appears in the number of a list 
def largestarray(array):
    numbers = {x:0 for x in array} # se crea un diccionario cuya llave son los números del array y los valores son las veces que lo hemos encontrado. 
    left = right = 0
    for number in array:
        if numbers[number] == 0:
            left_count = number-1
            right_count = number + 1 
            while left_count in numbers:
                numbers[left_count]= 1
                left_count-=1
            left_count +=1 
            while right_count in numbers:
                numbers[right_count]= 1
                right_count+=1
            right_count -=1 

            if (right-left)<=(right_count-left_count):
                right = right_count
                left = left_count
    return [left,right]            
#%%
person1_schedule = [['9:00','10:30'],['12:00','13:00'],['16:00','18:00']]
person1_boundaries = ['9:00','20:00']
person2_schedule = [['10:00','11:30'],['12:30','14:30'],['14:30','15:00'],['16:00','17:00']]
person2_boundaries = ['10:00','18:30'] # todas las posibles agendas deben estar dentro de este rango 

def time(time1, time2):
    hour1, min1 = time1.split(':')
    hour2, min2 = time2.split(':')

def calendarAvail(person1,person2):


#%%

# Some numbers have funny properties. For example:

# 89 --> 8¹ + 9² = 89 * 1

# 695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

# 46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

# we want to find a positive integer k, if it exists, such as the sum of the digits of n taken to the successive powers of p is equal to k * n.
# In other words:

# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

# If it is the case we will return k, if not return -1.

# Note: n and p will always be given as strictly positive integers.

# #def dig_pow(n, p):
#     n_string = str(n)
#     exp = range(p,len(n_string)+1)
#     current_sum = 0
#     for i in range(len(n_string)):
#         current_digit = int(n_string[i])
#         current_sum += current_digit**exp[i]
#     if (current_sum % n) == 0:
#         return(int(current_sum/n))
#     else:
#         return -1


#%%
# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

# def xo(s):
#     s = s.lower()
#     num_x = s.count("x")
#     num_o = s.count("o")
#     if (num_x >=1) or (num_o >=1):
#         if num_x == num_o:
#             return True
#         else:
#             return False
#     else :
#         return True 

#%%  Given two integers a and b, which can be positive or negative, find the sum of all the integers between including them too and return it. If the two numbers are equal return a or b.

#Note: a and b are not ordered!
# def get_sum(a,b):
#     if a == b:
#         return a 
    
#     elif b > 0:
#           rango = range(a,b+1)
#           suma = sum(list(rango))
#           return suma 
#     elif b < 0:
#         suma = b
#         return suma         

#%%
# def to_camel_case(text):
#     if ("_" in text):
#          string_normal = text.split("_")
#          if not string_normal[0].isupper():

#          string_normal = "".join(string_normal)   
#     else:
#         string_normal = text.split("-")
#         string_normal = "".join(string_normal)
#     return string_normal        

#%%
def to_camel_case(text):
    if text == '':
        return ''   
    elif '-' in text:
        if  not text[0].isupper():
            temp_text = text.split("-")
            resp_text = temp_text[0]+"".join(x.title() for x in temp_text[1:])
        else:
            text = text.split("-")
            resp_text = "".join(text)   
    elif '_' in text:
        if  not text[0].isupper():
            temp_text = text.split("_")
            resp_text = temp_text[0]+"".join(x.title() for x in temp_text[1:])
        else:
            text = text.split("_")
            resp_text = "".join(text)
    return resp_text         
#%%
# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

#It should remove all values from list a, which are present in list b keeping their order.

#If a value is present in b, all of its occurrences must be removed from the other:

def array_diff(a, b):
    for i in range(len(b)):
        for j in range(len(a)):  
            elemento_b = b[i]
            if not a :
                return a
            elif not b:
                return a 
            elif elemento_b in a:
                a = [num for num in a if num != elemento_b]    
    return a   

def array_diff(a, b):
    return [x for x in a if x not in b]                  
            
#%% Verificar si un número es 
def is_square(n):
    if n>=0:
        root = int(n**(1/2))
        if (root*root == n):
            return True
        else:
            return False
    else:
        return False      

import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;        

#%%

"In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its population greater or equal to p = 1200 inhabitants?"

#"p0, percent, aug (inhabitants coming or leaving each year), p (population to surpass)

"the function nb_year should return n number of entire years needed to get a population greater or equal to p.aug is an integer, percent a positive or null floating number, p0 and p are positive integers (> 0)"
def nb_year(p0, percent, aug, p):
    number_of_years = 0
    percent = percent/100
    current_population = p0
    while not (current_population >= p):
        current_population += int(current_population*(percent))+aug
        number_of_years+=1
    return number_of_years
    

#%%
def spin_words(sentence):
    split_sentence = sentence.split(" ")# las separamos por espacios
    new_sentence = []
    if len(split_sentence) == 1:
        if len(split_sentence[0])>=5:
            new_sentence = split_sentence[0][::-1]
        else:
            new_sentence = split_sentence[0]  
    else:
        for i in range(len(split_sentence)):
            if len(split_sentence[i])>=5:
                reversed = split_sentence[i][::-1]
                new_sentence.append(reversed)
            else:
                new_sentence.append(split_sentence[i])
        new_sentence = " ".join(new_sentence)          
    return new_sentence


def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])

    
#%%
import math
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise 
    # sq y su raiz deben ser integer 
    if math.sqrt(sq).is_integer():
        nextN = math.floor(math.sqrt(sq)) + 1
        return nextN * nextN
    else:
        return -1     

def find_next_square(sq):
    root = sq ** 0.5 # 11
    if root.is_integer():
        return (root + 1)**2 # 11+1 = 12**2 = 144
    return -1

#%% ISLAND PERIMETER 
island = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]    
print(type(island))
print(len(island))
print(len(island[0]))
print(island)
#%%
def islandPerimeter(grid):
        H = len(grid) # height filas
        W = len(grid[0]) # Width  columnas 
        def dfs(r,c):
            if r < 0 or r >= H or c < 0 or c >= W or grid[r][c] == 0 : # si me sali de las columnas o me sali de las filas o si el punto es agua 
                return 1 
            if grid[r][c] == 1:
                grid[r][c] = 2
                return dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1) 
            return 0 
        perimeter = 0
        for r in range(H):
            for c in range(W):
                if grid[r][c]==1:
                    perimeter += dfs(r,c)    

        return perimeter  

island = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]] 
islandPerimeter(island)
#%% REVERSED BITS 

bit = 0o1000100001000000000100000000010
def reversed_bit(bit):
    r = list("{:032b}".format(bit))
    r.reverse()

    return int("".join(r),2)

reversed_bit(bit)

#%%
def dirReduc(arr):
    direction = []

    for i in range(len(arr)):
        if  (arr[i] == "SOUTH" and arr[i+1] == " NORTH") or (arr[i] == "NORTH" and arr[i+1] == "SOUTH") or (arr[i] == "WEST" and arr[i+1] == "EAST") or (arr[i] == "EAST" and arr[i+1] == "WEST"):
            arr.pop(i)
            arr.pop(i+1)

#%%
def dirReduc(arr):
    dict = {"NORTH":"SOUTH","SOUTH":"NORTH","EAST":"WEST","WEST":"EAST"}
    direction = []
    for i in arr:
        if  direction and dict[i] == direction[-1]:
            direction.pop()
        else:
            direction.append(i)
    return direction

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
dirReduc(a)



#%%
var1 = 100
if var1:
   print (var1)
else:
  
   print (var1)


#%%
s = "()" 
print(s[1])

# #%%
# def valid_parentheses(string):
#     dict = { "(" : " )"}
#     for i in string:

#%%
a = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
max_sum = []
def max_sequence(a):   
    if a == []:
        return 0 
    else:        
        for i in range(len(a)):
            for j in range(len(a)):
                max_sum.append(sum(a[i:-j+1]))
    return max(max_sum)        

max_sequence(a)

#%% 
a = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
print(a[:])
#%%
a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
rango = range(len(a)+1)   
multiply_list = [element * -1 for element in rango]
max_sum = [sum(a)]
def max_sequence(a):   
    if a == []:
        return 0 
    else:
        for i in range(len(a)):
            for j in multiply_list:
                max_sum.append(sum(a[i:j]))    
    return max(max_sum)

max_sequence(a)

            
#%%
a = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
rango = range(len(a))   
multiply_list = [element * -1 for element in rango]
max_sum = []
def max_sequence(a):   
    if a == []:
        return 0 
    else:
        for i in range(len(a)):
            current_list = a[i:]
            max_sum.append(sum(current_list))
            for j in multiply_list:
                current_sequence = current_list[i:j]
                max_sum.append(sum(current_sequence))    
    return max(max_sum)

max_sequence(a)

#%% The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:
a = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
def max_sequence(a):   
    rango = range(len(a))   
    multiply_list = [element * -1 for element in rango]
    max_sum = []
    if a == []:
        return 0 
    else:
        for i in range(len(a)):
            current_list = a[i:]
            max_sum.append(sum(current_list))
            for k in range(len(current_list)):
                for j in multiply_list:
                    current_sequence = current_list[k:j]
                    max_sum.append(sum(current_sequence))
                continue 
            continue 
                
    return max(max_sum)

max_sequence(a)


#%%

m_s ="http://google.co.jp"
token = url.split('.')[0]
if 'http://' in token:
    token = token.split('/')[2]
else:
    token = url.split('.')[0]    



#%%
str = 'Hello world !'
splited = str.split(" ")
print((splited[0][1:]))
print(splited[0][0])
#%%
ay = "ay"
results = []
def pig_it(text):
    splited =text.split(" ")
    for i in splited:
        first = i[0]
        actual = i[1:]
        final = actual+first+ay
        results.append(final)

    result =  " ".join(results)     

    return result 

x = pig_it('Hello world !')
print(x)

#%%
def multi_table(number):
    for i in range(1,11):
        print(f"{i}*{number} = {i*number}")
multi_table(5)  

#%%
lista = []
def logical_calc(array, op):
    op = op.lower()
    for i in range(len(array)):
        lista.append(array[i])
        lista.append(op)
        lista.append(array[i+1])
        res = " ".join(lista)



    return bool 

array = [True, True, False] 
op = "AND"


#%%
op = "AND"
print(op.lower())
rest = False and True
print(type(res))

#%%
op = "AND"
lista = str(False) +" "+ str(op.lower())+" "+ str(True)
print(bool(lista)) 

#%%
def move_zeros(array):
    zeros = [0]*array.count(0)
    array = [value for value in array if value !=0] 
    array.extend(zeros)
    return array

move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])

#%%
lista = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
print(lista.count(0))
zeros = [0]* lista.count(0)
print(lista.remove(0))     

#%%
array = [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
array = [value for value in array if value !=0] 

#%%
# 3*2 = 6 3*3 = 9 5*1 = 5 3*1 = 3 
def solution(num):
    multiples = []
    numbers = [3,5]
    for i in numbers:
        for j in range(0,num):
            mult = i*j
            if mult<num:
                multiples.append(mult)
            else:
                continue    

#%%
def multiples(m, count):
    for i in range(count):
        print(i*m)
    
multiples(3,10)

#%%
def title_case(title, minor_words):
    title = title.split(' ') 
    word = [] 
    for i in title:
        if i in minor_words and i != title[0]:
            word.append(i.lower())
        else:
            word.append(i.capitalize())   
    return " ".join(word)
   
title_case('THE WIND IN THE WILLOWS', 'The In')   
    
#%%
a = "Juan"
print(a[0].isupper())      

#%%
str = "the king in the north"
str = str.split(' ')
#%%
str = "THE WIND IN THE WILLOWS"
st = []
str = str.split(" ")
print(str[0].capitalize())
# for i in str:
#     print(i.lower())

final = [i.capitalize() for i in str if i not in minor_words]
 
# %%
number = 8
factors = []

for whole_number in range(1, number + 1):
    if number % whole_number == 0: # si el residuo es igual a 0 
        factors.append(whole_number)

print((factors))
#%%
print(4%3)

#%%
a = [7,6,3,5,3,3,6,7]
print(list(set(a)))


#%%
d = {'x': 1, 'y': 2, 'z': 3} 
for key, value in d.items():
    print(key,value)


#%%
  
for i in input().split():
    rooms =[]
    rooms.append (int(i)) 

print(rooms)

#%%
d = dict.fromkeys(a, 0)
print(d)

#%%
a = [1,5,16,14,4,1]
#a = [8,2,2,30,15]
pos = a[0]
new_arrange = a[2:]
print(new_arrange)
sum = [x+pos for x in new_arrange] # el indice del que dio el mayor el índice de 16 
max_sum = max(sum)
print(max_sum)
max_index = sum.index(max_sum)
print(max_index)
print(new_arrange[max_index])
max_number = new_arrange[max_index] 
indice_maximo = a.index(max_number)
print(a[indice_maximo])
new_arrange = a[indice_maximo+2:]
print(new_arrange)
sum = [x+pos for x in new_arrange] # el indice del que dio el mayor el índice de 16 
max_sum = max(sum)
print(max_sum)
max_index = sum.index(max_sum)
print(max_index)
print(new_arrange[max_index])
max_number = new_arrange[max_index] 
indice_maximo = a.index(max_number)
print(a[indice_maximo])

