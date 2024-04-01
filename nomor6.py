for i in range(4):
	for j in range(5):
		if (i + j) % 2 == 0:
			print("A", end=" ")
		if (i + j) % 2 == 1:
			print("B", end=" ")
	print()