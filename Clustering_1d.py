import numpy as np
"""
Alg 1:
DOESN'T WORK FOR DATA BELOW
data = [1, 5, 10, 16]
DOES WORK FOR DATA BELOW
data = [1, 2, 4, 9, 10, 12]
Step 1:
Find median of the data set.
Step 2:
Minus each data point from it's previous one(2-1, 4-2, 9-5, etc...)
Step 3:
If it is above the median, add a cluster group

Alg 2:
data = [1, 5, 10, 16]
data = [1, 2, 4, 9, 10, 12]
Step 1:
Minus each data point from its previous data point 5-1, 10-5, etc..., then 
append each value to a data set (pref called gaps)
Step 2:
Find the biggest gap in the gaps data set, and then correlate its corresponding
data points in the original data set (using np.argmax to find the position)
Step 3: 
Anyt number below and equal to the number that corresponds to the argmax output
goes into one cluster, while everything else goes into another.
"""
# data = np.array([1, 5, 17, 20, 12, 3, 7])
# data = np.array([1, 9, 4, 7, 11])
data = np.array([1, 9, 3, 14, 2, 12])
gaps = []
cluster1 = np.array([])
cluster2 = np.array([])

# Finding all the differences and appending them to gaps array(step 1).
for i in range(len(data)):
    if i!= 0:
        gaps.append(data[i]-data[i-1])

# Split is to find the position of the biggest gap; splitmean is to find the 
# mean of the corresponding 2 numbers (both step 2).
split = np.argmax(gaps)
splitmean = (data[split]+data[split+1])/2

# Appending anything below the mean to cluster1, and anything above to cluster2
# (step 3).
for i in range(len(data)):
    if data[i] < splitmean:
        cluster1 = np.append(cluster1, data[i])
    else: 
        cluster2 = np.append(cluster2, data[i])
    
            
    
