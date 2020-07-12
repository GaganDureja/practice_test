# increasing order function
def increse_order(subarray):	
	for element in range(len(subarray)):
		for element1 in range(element + 1, len(subarray)):
			if len(subarray[element]) > len(subarray[element1]):
				subarray[element], subarray[element1] = subarray[element1], subarray[element]
	return subarray

# define a array
num_array = [1,2,4,9,0,-1,6,7,2,3,4,5,6,7,4,3,7,0]

# initialize a list of list with first item from num_array
result = [[num_array[0]]]

for number in num_array[1:]:  # start loop with second item
    if result[-1][-1] < number:  # append to last list
        result[-1].append(number)
    else:
        result.append([number])  # create a new list/ 2d array

# sort by length and get last item
print(increse_order(result)[-1])
