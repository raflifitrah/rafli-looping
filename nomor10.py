for i in range(7):
	for j in range(7):
		print("1"
			if j == i
			or j == 6 - 1
			else "+", end=" ")
	print()