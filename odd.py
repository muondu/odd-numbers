a = int(input("Enter the number you want to start with:  "))
b = int(input("Enter the number you want to end with:  "))
for dub in range(a,b):
	while dub % 2 == 0:
		dub += 1
		print(dub)