
items=[]
prod=1
for i in range(5):
	print (f"Enter price for item { i+1} : ")
	p=int(input())
	items.append(p)
for j in range(len(items)):
	print(f"Price for item {j+1} = Rs. {items[j]}")
	prod = prod * items[j]
print("Sum of all prices = Rs.", sum(items))
print("Product of all prices = Rs.", prod)
print("Average of all prices = Rs.",sum(items)/len(items))