#https://www.youtube.com/playlist?list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATf
#https://leetcode.com/list/xi4ci4ig/ lista de las 75 preguntas 
#%% TWO SUM - LEETCODE 1 
# return the indices of two numbers that sum to the target 
# Problema de tipo Hashmap 
# mapeamos los valores del array a sus correspondientes índices. 
# añadimos el valor-índice al hasmap una vez no hayamos encontrado el otro número que le sume para el target.
# Prev = {llave(número): value(índice dentro del array de ese número)}

def two_sum(numbers,target):
    prev = {}
    for index,number in enumerate(numbers):
        if target-number  in prev:
            return [prev[target-number],index]
        prev[number] = index

two_sum([2,6,4,5,9],6)

# Time Complexity O(n)
# Space complexity O(n)
#%% BEST TIME TO BUY AND SELL A STOCK 
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
# cada vez que avanzo ya no puedo tener en cuenta el día anterior 
# debo buscar la máxima diferencia en cada subarray 
# Idealmente debe haber un número mayor que yo dentro del subarray 
# PROBLEMA DEL TIPO TWO POINTERS : UNO A LA IZQUIERDA DEL ARRAY Y OTRO A LA DERECHA 
# LOS POINTERS SERÁN L: DÍA QUE COMPRO R: DÍA QUE VENDO 
# SI el valor que está en el pointer R es menor al valor en el pointer L pues paila mejor comprar a dicho valor menor 
# Actualizamos los pointers 

def buy(prices):
    l,r = 0,1 # left: buy , right : selling 
    maxp = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r]-prices[l]
            maxp = max(maxp,profit)
        else:
            l = r
        r+=1    
    return maxp 

prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]


def maxProfit(self, prices):
        profit, min_buy = 0, float('inf') 
        for price in prices:
            min_buy = min(min_buy, price) #is price less than min_buy
            profit = max(profit, price - min_buy)
        return profit

# Time Complexity O(n) : two pointers 
# Space complexity O(1) . solo se declaran variables constantes como los pointers 


#%% Product of Array Except Self

"""

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

def product_notself(nums):
    res = [1]*len(nums)
    prefix = 1
    posfix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]
    
    for i in range(len(nums)-1,-1,-1):
        res[i] *= posfix
        posfix *= nums[i]    
    return res 

product_notself(nums = [1,2,3,4])

# Time complexity O(n)
# Space complexity O(1)

#%%
# MAXIMUM SUB ARRAY 

"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

"""

# left and right pointer 
# kind of a sliding window 


def max_subarray(nums):
    max_sub = nums[0]
    final_sum = 0
    for n in nums:
        if final_sum < 0:
            final_sum = 0
        final_sum += n
        max_sub = max(max_sub,final_sum) # con este max nos desasemos de los números anteriores si estos restan a nuestra suma total. 
        
    return max_sub        

max_subarray(nums = [-2,1,-3,4,-1,2,1,-5,4])


# Time complexity O(n)
# Space complexity O(1)
