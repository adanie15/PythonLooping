for x in range(1,10):
	print(x)
	print(x*x)
# 1
# 1
# 2
# 4
# 3
# 9
# 4
# 16
# 5
# 25
# 6
# 36
# 7
# 49
# 8
# 64
# 9
# 81

for letter in "coffee":
	print(letter*10)
# cccccccccc
# oooooooooo
# ffffffffff
# ffffffffff
# eeeeeeeeee
# eeeeeeeeee 

for nums in range(10,20,2):
	print(nums)
# 10
# 12
# 14
# 16
# 18 

times = input("How many times do I have to tell you? ")
times = int(times)

for time in range(times):
	print("TAKE OUT THE GARBAGE!")



######################### EVEN, ODD OR UNLUCKY NUMBERS EXERCISE #########################

for x in range(1,21):
	if x == 4 or x == 13:
		print(f"{x} is UNLUCKY!")
	elif x % 2 == 0:
		print(f"{x} is even")
	else:
		print(f"{x} is odd")

for x in range(1,21):
	if x == 4 or x == 13:
		state = "UNLUCKY!"
	elif x % 2 == 0:
		state = "even"
	else:
		state = "odd"
	print(f"{x} is {state}")