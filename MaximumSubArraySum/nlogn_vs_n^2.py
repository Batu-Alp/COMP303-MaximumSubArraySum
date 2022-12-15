from time import time
from random import randint
import numpy as np
import sys
import matplotlib.pyplot as plt

arr1 = np.random.randint(-100,100,10)
arr2 = np.random.randint(-100,100,50)
arr3 = np.random.randint(-100,100,100)
arr4 = np.random.randint(-100,100,500)
arr5 = np.random.randint(-100,100,1000)
arr6 = np.random.randint(-100,100,5000)
arr7 = np.random.randint(-100,100,10000)
arr8 = np.random.randint(-100,100,50000)
arr9 = np.random.randint(-100,100,100000)
all_arrays = np.array([arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9])
arr_sizes = [10,50,100,500,1000,5000,10000,50000,100000]
running_times_brute_force = []
running_times_divide_and_conquer = []

def maxSubArraySumBruteForce(arr):        
    max_sum = -sys.maxsize
    start = 0
    end = 0
 
    for i in range(len(arr)):
        sum = 0        
        for j in range(i, len(arr)):
            sum += arr[j]
 
            if sum > max_sum:
                max_sum = sum
                start = i
                end = j
    return max_sum, start, end

def maxSubArraySumDivideAndConquer(arr):        


    def maxCrossingSubarraySum(arr, low, mid, high):
        
        left_sum = float('-inf')
        sum = 0
        cross_start = mid
        for i in range(mid - 1, low - 1, -1):
            sum = sum + arr[i]
            if sum > left_sum:
                left_sum = sum
                cross_start = i
            
        right_sum = float('-inf')
        sum = 0
        cross_end = mid + 1
        for i in range(mid, high):
            sum = sum + arr[i]
            if sum > right_sum:
                right_sum = sum
                cross_end = i + 1
        
        return cross_start, cross_end, left_sum + right_sum


    def maxSubArraySum(arr, low, high):          
        
        if low == high - 1:
            return low, high, arr[low]
        else:
            mid = (low + high) // 2
            left_start, left_end, left_max = maxSubArraySum(arr, low, mid)
            right_start, right_end, right_max = maxSubArraySum(arr, mid, high)
            cross_start, cross_end, cross_max = maxCrossingSubarraySum(arr, low, mid, high)
            if (left_max > right_max and left_max > cross_max):
                return left_start, left_end, left_max
            elif (right_max > left_max and right_max > cross_max):
                return right_start, right_end, right_max
            else:
                return cross_start, cross_end, cross_max
        
    low = 0
    high = len(arr) - 1
    return maxSubArraySum(arr,low,high)

for i in all_arrays:
    time0 = time()
    maxSubArraySumBruteForce(i)
    time1 = time()
    maxSubArraySumDivideAndConquer(i)
    time2 = time()
    print("For n : ", len(i))
    print ("n^2:", time1-time0)
    print ("nlogn:", time2-time1 )
    print()



