
def insertion_sort(list):
	for i in range(1,len(list)):
		x = list[i]
		j = i-1
		while (j != -1 and list[j] > x):
			list[j+1] = list[j]
			j-=1
		list[j+1] = x
	return list

a = [2,7,4,1,5,3]
print(a)
insertion_sort(a)
print(a)
