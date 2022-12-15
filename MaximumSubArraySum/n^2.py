import sys
import time
import numpy as np
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
running_times = []

 
def findMaximumSum(arr):
 
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
 
 
for i in all_arrays:
    st = time.time()
    max_sum, start , end = findMaximumSum(i)
    et = time.time()
    print("Size of the array : %d" % (len(i)))
    print("Maximum contiguous sum : %d" % (max_sum))
    print("Starting Index : %d" % (start))
    print("Ending Index : %d" % (end))
    elapsed_time = et - st
    final_res = elapsed_time * 1000
    print('Execution time:', elapsed_time, 'seconds')
    print('Execution time:', final_res, 'milliseconds\n')
    running_times.append(elapsed_time)


plt.plot(arr_sizes, running_times)
plt.title("n^2")
plt.xlabel("Array Sizes")
plt.ylabel("Running Times")
plt.show()