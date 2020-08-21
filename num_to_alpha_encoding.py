def encode(num):	
	txt='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	result = ''
	
	while num>0:
		alpha_index = (num-1)%26
		result+= txt[alpha_index]
		num = (num-1)//26
	return result[::-1]






print(encode(1379))