
def twoSum(nums, target):
    dic = {} # crea un diccionario 
    for i, n in enumerate(nums): 
        if n in dic: # si n está como llave en ese diccionario 
            return [dic[n], i] # devuelva el valor correspondiente a esa llave y la posición i 
        dic[target-n] = i # de lo contrario adicione una llave que sea igual a  target-n y su value es i 

# en la primera i= 0 y n = 2 

# como n=2 no está como llave en el diccionario, se guarda en este el residuo entre 9-n = 7 como llave y 0 como value 

twoSum(nums = [3,2,4], target = 6)


def roman_to_integer(s):
    roman_dic = {'I' : 1, 'V' : 5, 'X':10,'L':50, 'C':100, 'D' : 500, 'M' : 1000}
    z = 0
    for i in range(len(s)):
        if roman_dic[s[i]] < roman_dic[s[i+1]]:
            z -= roman_dic[s[i]]
        else: 
            z += roman_dic[s[i]]

    return z + roman_dic[s[-1]]


def romanToInt(s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            z -= roman[s[i]] # le quita a lo que haya en z la cantidad correspondiente a la llave i 
        else:
            z += roman[s[i]]
    return z + roman[s[-1]] # el último valor del número romano si o si debe estar en el diccionario  
#romanToInt("MCMXCIV")    




def romanToInt(s: str) -> int:
    roman_to_int = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    
    result = 0
    prev_value = 0
    for letter in s:
        value = roman_to_int[letter] #1000 
        result += value # 0+= 1000
        if value > prev_value:
            # preceding roman nummber is smaller
            # we need to undo the previous addition
            # and substract the preceding roman char
            # from the current one, i.e. we need to
            # substract twice the previous roman char
            result -= 2 * prev_value
        prev_value = value  
    return result

romanToInt("MCMXCIV")       



def majorityElement2(nums):
        m = {}
        for n in nums:
            m[n] = m.get(n, 0) + 1 # m.get(n,0) es retorne el valor para la llave n, de no ser así retorne 0 +1 
            # esto practicamente cuenta cuantas veces aparece el número n en la lista, en cada iteración va sumando 1 
            if m[n] > len(nums)//2:
                return n

majorityElement2(nums = [2,2,1,1,1,2,2])      

def majorityElement2(nums):
    return sorted(nums)[len(nums)//2]

majorityElement2(nums = [2,2,1,1,1,2,2])   
#print(sorted(nums))



nums = [2,2,1,1,1,2,2]
print(len(nums)//2) # floor division 


#%%
def longest_sub(s):
    used = {}
    max_length = start = 0
    for i, c in enumerate(s):
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            max_length = max(max_length, i - start + 1)
            
        used[c] = i
    return max_length

longest_sub("abcabcbb")    

#%%
from collections import Counter

def findRepeatedDnaSequences(s):
    counter = Counter(s[i:i+10] for i in range(0, len(s) - 9))
    # toma un pedazo de secuencia desde 0 hasta 10 por ejemplo y cuenta cuantas veces apareció 
    # luego sigue al siguiente subpedacito desde 1 hasta 11 
    print(counter)
    return [key for key in counter if counter[key] > 1]

findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')    
s = 'AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'
x = list(range(0,len(s)-9))
print(x[-1])
print(len(s))


#%%
from collections import Counter

def findRepeatedDnaSequences(s):
    counter = []
    for i in range(0,len(s)-9):
        counter += Counter(s[i:i+10])
    
    keys = []
    for key in counter:
        if counter[key] > 1:
            keys.append(key)
    return keys

findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')  


#%%
from collections import  defaultdict
someddict = defaultdict(int) # si no encuentra la llave 3 muestra un 0 
print(someddict[3]) # print int(), thus 0
print(someddict.keys())
print(someddict.values())
print(someddict.items())

#%%
from collections import Counter
myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
print (Counter(myList)) # cuenta cuantas veces a aparecido un elemento en la lista 
# el número 2 aparece 4 veces y así. 

#%%
from collections import  deque
# PRIMERO ES IZQUIERDA ÚLTIMO ES DERECHA 
my_queue = deque()
my_queue.append(5)
my_queue.append(10)
my_queue.append(15)
print(my_queue[2])
print(type(my_queue))
my_queue.popleft() # el primero que entra es el primero que sale FIFO 
print(my_queue)
my_queue.appendleft(6) # lo mete de primero 
print(my_queue)
my_queue.popleft() # el primero que entra es el primero que sale FIFO 
print(my_queue)
my_queue.clear() # borra todos los elementos 
print(my_queue)


#%%
def findSubstring(s, words):
    from collections import deque, defaultdict, Counter
    s_len  = len(s) # longitud del string 
    word_len = len(words[0]) # len(foo) = 3 
    word_len_total = len(words) * word_len  # len( ["foo","bar"]) * len(foo) = 2*3 = 6 
    count = Counter(words) # 1 para foo y 1 para bar 
    footprint = defaultdict(deque) # un default dict en donde el tipo de valor de sus values es un queue. 
    result = [] # donde se almacenarán los indices 
    for start in range(word_len): # desde 0 hasta 3 sin el 3 
        footprint.clear() 
        end = start # fin es igual al principio 
        while start + word_len_total <= s_len: # (start = 0 + word_len_total = 6) <= (s_len = 18)
            sub = s[end:end+word_len] # sub = s[0:3] = 'bar' para la primera iteración 
            end += word_len # end = 3 
            if sub in count: # si 'bar' esta como llave en count (si está)
                queue = footprint[sub]  # el valor de la llave sub en el diccionario footprint , footprint['bar']
                                        # a la variable queue asignele lo que haya en el valor de la llave sub , esto será un queue 
                queue.append(end) # agregue el número 3 
                while queue[0] < start: # 3 es menor que start ? 3 es menor que 0 no 
                    queue.popleft()
                if len(queue) > count[sub]:
                    start = queue.popleft()
                if start + word_len_total == end:
                    result.append(start)
            else:
                start = end
    return result

findSubstring(s = "barfoothefoobarman", words = ["foo","bar"])    

#%%
from collections import deque, defaultdict, Counter
footprint = defaultdict(deque)
print(footprint)
#%%
x =(range(3))
for i in x :
    print(i)

#%%
def sq(num):
    suma = {}
    while suma != 0:
        num_str = list(str(num)) # convertimos el numero a str 
        suma = sum([int(i)**2 for i in num_str]) # obtenemos la suma de sus dígitos al cuadrado 
        return suma
sq(17)   

#%%
def isHappy(n):
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum([int(x) **2 for x in str(n)])
        return n == 1

isHappy(19)        
# %%

a = set()
a.add(3)

#%% HEAP QUEUE 
#You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

#Return the max sliding window.

def max_window(nums,k):
    original_len = k
    w_s = k # window size
    max_numbers =[]
    for i in range(len(nums)):
        actual = nums[i:w_s] 
        if len(actual) == original_len:
            max_num = max(actual)
            w_s+=1
            max_numbers.append(max_num) 
    return max_numbers


max_window(nums = [9,11], k = 2)

#%%
import heapq
from heapq import heappush, heappop
li = [5, 7, 9, 1, 3]
print("The original list is:",end="")
print(li)
heapq.heapify(li)
print ("The created heap is : ",end="")
print (list(li))
# using heappush() to push elements into heap
# pushes 4
heapq.heappush(li,4)
# printing modified heap
print ("The modified heap after push is : ",end="")
print (list(li)) 
# using heappop() to pop smallest element
print ("The popped and smallest element is : ",end="")
print(heapq.heappop(li))
print(list(li))

#%%
import heapq
from heapq import heappush, heappop
def minInterval(intervals, queries):
		# To store the output result
        lis = [0 for i in range(len(queries))] # una lista de 0's 
		#sort the intervals in the reverse order
        intervals.sort(reverse = True) # de mayor  a menor  
		#View the intervals list
        print(intervals)
		#store the index number of the query with query number
        queriesWithIndex = sorted([(q,i) for i,q in enumerate(queries)])
		#Print and view the queriesWithInd
        print(queriesWithIndex)
		#decare the lis to store the valuew but with the help of heap so the it will be store in sorted form
        heapLis = []
		#Traverse the queryWithIndex list which consists of tuples
        for query,i  in queriesWithIndex:
            # query = 2 , i = 0 
			# loop should run till the intervals becomes empty
            while len(intervals)  and query >=intervals[-1][0]:
                                      # 2 >= 1 
				#pop the last value from interval and store it in start and end value
                start, end = intervals.pop()
                # start 1, end 4 
				#push the value in the heap list
                heappush(heapLis,[end - start + 1, end])
			# traverse till the heaplis becomes empty or the element in heapLis[0][1] < query
            while len(heapLis) and heapLis[0][1] < query:
                heappop(heapLis)
                #pop the tuple from the heapLis
			#if len(heapLis) is 0 then simply assign lis to -1 else assign the value of heapLis[0][0] to lis[i]
            if len(heapLis) == 0:
                lis[i] = -1
            else:
                lis[i] = heapLis[0][0]
		#return the lis
        return lis

minInterval(intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5])


#%%

# Python program to reverse a string using recursion
 
# Function to print reverse of the passed string
def reverse(string):
    if len(string) == 0:
        return
     
    temp = string[0]
    reverse(string[1:])
    print(temp, end='')
 
# Driver program to test above function
string = "Geeks for Geeks"
reverse(string)


#%%
from collections import Counter
def long_sub(s,k):
    counter = Counter(s)
    total = 0
    for value in counter.values():
        if value >= k:
            total += value
    return total

#%%
from collections import Counter
def long_sub(s,k):
    counter = Counter(s)
    total = sum([value for value in counter.values() if value >= k])
    return total

long_sub("ababacb" ,3)

#%%
import statistics
def max_window(nums,k):
    original_len = k
    w_s = k # window size
    median_numbers =[]
    for i in range(len(nums)):
        actual = nums[i:w_s] 
        if len(actual) == original_len:
            mediana = statistics.median(actual)
            w_s +=1
            median_numbers.append(mediana) 
    return median_numbers


max_window(nums = [1,2,3,4,2,3,1,4,2], k = 3)

#%%
import heapq
from heapq import heapify, heappush
def kesimo_mayor(nums,k):
        pq = nums[:k] # tome las primeras k posiciones 
        #pq = [3,2]
        heapq.heapify(pq) # conviertalo en un heap, min heap 
        # [2,3]
        for x in nums[k:]: # [1,5,6,4]
            heapq.heappush(pq, x) # mete ese número al heap, si es menor 
            heapq.heappop(pq)# el número menor que esté en el heap lo saca 
        return pq[0] # al final la lista siempre tendra 2 elementos y devuelve el menor de ellos 

kesimo_mayor(nums = [3,2,1,5,6,4], k = 2)
#%%
nums = [3,2,1,5,6,4]
print(nums[1:3]) # no se incluye al último elemento. 
#%%


def mettings (intervals): 
    intervals.sort(key = lambda a : a[0]) # organize los datos con base a un criterio y este es el número inicial de cada tupla.
    for i in range(1,len(intervals)):
        i1 = intervals[i-1] # la tupla anterior 
        i2 = intervals[i] # la tupla actual
        
        if i1[1] >= i2[0]: # si el final del anterior es mayor que el inicio del que estamos 
            return False
    return True # si después de acabar todo el recorrido nunca pasó la condición pasada podemos decir true.     
        

#%%
import heapq
from heapq import heappush, heappop,heapify
intervals = [(5,10),(15,20),(0,30)]
intervals.sort(key = lambda a : a[0])
heapify(intervals)
print(type(intervals))

#%%
import heapq
from heapq import heappush, heappop,heapify
def mettings_two(intervals):
    intervals.sort(key = lambda a : a[0]) # organize los datos con base a un criterio y este es el número inicial de cada tupla.
    end_times = [intervals[i][-1] for i in range(len(intervals))]    
    heapify(end_times)    
    for i in range(len(intervals)):
        current_start = intervals[i][0]
        earliest_end = heappop(end_times)
        
        if current_start >= earliest_end:
            intervals[i][-1] = none
            
        
#%%
def wordbreak(s, wordDict):
    dp = [False]*(len(s)+1)
    dp[len(s)]= True
    
    for i in range(len(s),-1,-1):
        for w in wordDict:
            if (i+len(w)) <= len(s) and s[i:i+len(w)] == w:
                dp[i] = dp[i+len(w)]
            if dp[i]:
                break
    return dp[0]            
                
wordbreak(s = "applepenapple", wordDict = ["apple","pen"])               

#%%
def longpalin (s):
    pal = ""
    pallen= 0
    for i in range(len(s)):
        # impares
        l,r = i,i
        while l >=0 and r < len(s) and s[l] == s[r]:
            if (r-l +1) > pallen:
                pal = s[l:r+1]
                pallen = len(pal)
            l-=1
            r+=1
        # pares
        l,r = i,i+1
        while l >=0 and r < len(s) and s[l] == s[r]:
            if (r-l +1) > pallen:
                pal = s[l:r+1]
                pallen = len(pal)
            l-=1
            r+=1         
    return pal        
        
longpalin("abcacd")    

#%%
def islandperimeter(grid):
    visited_lands = set()
    rows = len(grid)
    columns = len(grid[0])
    def dfs(i,j): # i for rows , j for columns 
        if i >= rows or j >= columns or i < 0 or j < 0 or grid[i][j]==0:
            return 1
        if (i,j) in visited_lands:
            return 0
        visited_lands.add((i,j))
        perimeter = dfs(i,j+1) 
        perimeter += dfs(i,j-1)  
        perimeter += dfs(i-1,j) 
        perimeter += dfs(i+1,j)
        
    for i in range(rows):
        for j in range(columns):
            if grid[i][j]:
                return dfs(i,j)    
            
            
#%%

def palindrome_number(x):
    if x<0: return False
    
    div = 1
    while x >= 10*div:
        div*=10
    while x:
        right = x%10
        left = x // div 
        if left!= right: return False
        
        x = (x%div) //10
        div = div/100
        
    return True

palindrome_number(123321)       

#%%
# Number of islands 

from collections import deque
def number_islands(grid):
    if not grid:
        return 0
    
    visited = set()
    rows = len(grid)
    columns = len(grid[0])
    n_islands = 0
    
    def bfs(r,c):
        q = deque()
        visited.add((r,c)) # add to the visited set that position r,c 
        q.append((r,c))
        
        while q :
            row , col = q.popleft()
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            
            for dr,dc in directions:
                if ((r+dr) in range(row)) and ((c+dc) in range(col)) and (grid[r+dr][c+dc] == "1") and ((r+dr, c+dc) not in visited):
                    q.append((r+dr,c+dc))
                    visited.add((r+dr,c+dc))
                    
        
    
    for r in range((rows)):
        for c in range(columns):
            if grid[r][c] == "1" and (r,c) not in visited:
                bfs(r,c) # run bfs in this cell 
                n_islands +=1 
    
    return n_islands
    
                    
                      