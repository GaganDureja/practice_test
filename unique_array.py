# Unique function
def unique(array):
	new_array = []
	for element in array:
		if element not in new_array:
			new_array.append(element)	
	return new_array


num_array = [1,2,4,9,0,1,5,1]
result = unique(num_array)
print("Input array: ", num_array)
print("Unique array: ", result)