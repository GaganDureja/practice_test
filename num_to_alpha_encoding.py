def encode(num):	
	txt='ZABCDEFGHIJKLMNOPQRSTUVWXYZ'
	last = num%26 if num%26 else 26 #get the last aplhabet of result
	multiples = [[last,1]] # last is confirmed now find rest 
	answer = txt[last] # adding the result
	
	while sum([x*y for x,y in multiples])!=num:

		if (num - sum([x*y for x,y in multiples]))/26 <=26:	
			
			answer+= txt[(num - sum([x*y for x,y in multiples]))//26]		
			multiples.append([(num - sum([x*y for x,y in multiples]))//26,26])			

		else:

			answer+= 'A'
			multiples.append([26,26])

	return answer[::-1]
		




print(encode(27))
print(encode(702))
print(encode(704))
print(encode(10004))
