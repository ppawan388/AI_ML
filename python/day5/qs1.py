import math
def is_prime(num):
	if num<=1:
		return false
	div=math.floor(math.sqrt(num))
	for i in range(2,div+1):
		if num%i==0:
			return False
	return True
num=3
count=0
while(count!=20):
	result=is_prime(num)
	if result==True:
		print(num)
		count=count+1
		
	num+=1

