import random
import time
import csv
import matplotlib.pyplot as plt

#Quicksort function  
def quicksort( aList ):
    _quicksort( aList, 0, len( aList ) - 1 )

#Quicksort Algorithm Implementation	
def _quicksort( aList, first, last ):
    if first < last:					
      pivot = partition( aList, first, last )
      _quicksort( aList, first, pivot - 1 )
      _quicksort( aList, pivot + 1, last )
 
#Partition fn - To do seperate numbers < pivot on left of it and numbers > pivot on right of it used in quicksort algo   
def partition( aList, first, last ) :
	#Selecting random pivot from list
    pivot = first + random.randrange( last - first + 1 )
	#Store pivot value in last
    swap( aList, pivot, last )
	#Loop uses divide and conquer approach
    for i in range( first, last ):
	  #If current number is greater than last no,swap and move ahead
      if aList[i] <= aList[last]:
        swap( aList, i, first )
        first += 1
	#Swap after dividing with pivot 
    swap( aList, first, last )
	#Return the pivot position
    return first
 
#Swap function  
def swap( A, x, y ):
  A[x],A[y]=A[y],A[x]

#Time Analysis function for quicksort algorithm  
def quickSortAnalysis():
	#Initializing dictionary for storing key-value pairs as size-time pairs for each list
	d = dict()
	#Generating random numbers list of size 100,200,300...10000.....100000
	for i in range(1,1001,1):
		lst = random.sample(range(100000),100*i)
		#Recording time just before starting quicksort
		start_time = time.clock()
		#Recording time difference after quicksort completed
		quicksort(lst)
		#Storing key-value pairs of size-time for each list
		d[len(lst)] = time.clock() - start_time
	
	#Writing key-value pairs as row-col values in an excel csv file	
	with open('mycsvfile.csv', 'wb') as f:
        	w = csv.DictWriter(f, d.keys())
        	w.writeheader()
        	w.writerow(d)
    return d

#Fn returns a dictionary of all key-value pairs of size-time values		
d = quickSortAnalysis()

#Plotting dict as x-y values on a graph
fig = plt.figure()
for data_dict in d.values():
   z=data_dict
   x = d.keys()[d.values().index(z)]
   y = data_dict
   plt.scatter(x,y)

fig.suptitle('Time Analysis', fontsize=20)
plt.xlabel('Size Of Array', fontsize=16)
plt.ylabel('Time(s)', fontsize=16)
fig.savefig('Time Analysis.png')
plt.show()

